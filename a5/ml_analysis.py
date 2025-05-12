from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.sql.functions import col

# 1. Initialize Spark
spark = SparkSession.builder.appName("IncomePrediction").getOrCreate()
print("SparkSession created successfully.")

# 2. Load data
cols = ["age","workclass","fnlwgt","education","education_num","marital_status",
        "occupation","relationship","race","sex","capital_gain","capital_loss",
        "hours_per_week","native_country","income"]
df = spark.read.csv("data/adult.data", header=False, inferSchema=True).toDF(*cols)
print(f"Dataset loaded with {df.count()} rows and {len(df.columns)} columns")

# Show data sample
print("\n=== DATA SAMPLE ===")
df.show(5)

# 3. Basic statistics
print("\n=== INCOME DISTRIBUTION ===")
df.groupBy("income").count().orderBy("count", ascending=False).show()

# 4. Preprocess: index categorical columns
categorical = ["workclass","education","marital_status","occupation","relationship","race","sex","native_country"]
for c in categorical:
    df = StringIndexer(inputCol=c, outputCol=c+"_idx").fit(df).transform(df)

# 5. Assemble features
feature_cols = ["age","education_num","hours_per_week"] + [c+"_idx" for c in categorical]
print("\n=== FEATURES USED ===")
print(feature_cols)
assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
data = assembler.transform(df).withColumn("label", 
    (col("income") == " >50K").cast("double"))

# 6. Train/test split
train, test = data.randomSplit([0.7,0.3], seed=42)
print(f"\nTraining set: {train.count()} rows")
print(f"Test set: {test.count()} rows")

# 7. Train logistic regression
lr = LogisticRegression(maxIter=10)
model = lr.fit(train)
print("\n=== MODEL TRAINED ===")

# 8. Feature importance
print("\n=== FEATURE IMPORTANCE ===")
weights = model.coefficients.toArray()
feature_importance = list(zip(feature_cols, weights))
sorted_importance = sorted(feature_importance, key=lambda x: abs(x[1]), reverse=True)
print("Top 5 most predictive features for income >50K:")
for feature, weight in sorted_importance[:5]:
    print(f"{feature}: {weight:.4f}")

# 9. Evaluate model
trainingSummary = model.summary
train_accuracy = trainingSummary.accuracy
print("\n=== MODEL EVALUATION ===")
print(f"Training accuracy: {train_accuracy:.4f}")
print(f"Test accuracy: {model.evaluate(test).accuracy:.4f}")
print(f"AUC: {trainingSummary.areaUnderROC:.4f}")

# 10. Confusion matrix
print("\n=== CONFUSION MATRIX ===")
predictions = model.transform(test)
tp = predictions.filter((col("prediction") == 1.0) & (col("label") == 1.0)).count()
fp = predictions.filter((col("prediction") == 1.0) & (col("label") == 0.0)).count()
tn = predictions.filter((col("prediction") == 0.0) & (col("label") == 0.0)).count()
fn = predictions.filter((col("prediction") == 0.0) & (col("label") == 1.0)).count()

print(f"True Positives: {tp} | False Positives: {fp}")
print(f"False Negatives: {fn} | True Negatives: {tn}")
precision = tp / (tp + fp)
recall = tp / (tp + fn)
f1 = 2 * precision * recall / (precision + recall)
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")

# 11. Sample predictions with demographics
print("\n=== SAMPLE PREDICTIONS ===")
sample_preds = predictions.select(
    "age", "education", "education_num", "hours_per_week", 
    "occupation", "label", "prediction"
).limit(10)
sample_preds.show()

# 12. Income by education level
print("\n=== INCOME BY EDUCATION ===")
edu_income = df.groupBy("education").pivot("income").count().fillna(0)
edu_income = edu_income.withColumn(
    "pct_high_income", 
    col(" >50K") / (col(" >50K") + col(" <=50K")) * 100
).orderBy("pct_high_income", ascending=False)
edu_income.show(10)

# 13. Income by hours worked
print("\n=== INCOME BY HOURS WORKED ===")
df.withColumn(
    "hour_group", 
    (col("hours_per_week") < 30).cast("int") * 1 + 
    ((col("hours_per_week") >= 30) & (col("hours_per_week") <= 40)).cast("int") * 2 +
    ((col("hours_per_week") > 40) & (col("hours_per_week") <= 50)).cast("int") * 3 +
    (col("hours_per_week") > 50).cast("int") * 4
).groupBy("hour_group").pivot("income").count().fillna(0).orderBy("hour_group").show()

spark.stop()
