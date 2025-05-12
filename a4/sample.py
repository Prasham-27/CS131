from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import DecisionTreeRegressor
from pyspark.ml import Pipeline
from pyspark.ml.evaluation import RegressionEvaluator

# Start Spark session
spark = SparkSession.builder.appName("NYC Taxi MLlib").getOrCreate()

# Load CSV
df = spark.read.csv("2019-01-h1.csv", header=True, inferSchema=True)

# Select required columns
selected = df.select(
    df.columns[3],   # passenger_count (4th col)
    df.columns[7],   # pulocationid (8th col)
    df.columns[8],   # dolocationid (9th col)
    df.columns[16],  # total_amount (17th col)
)

# Rename columns for clarity (optional but helpful)
selected = selected.withColumnRenamed(df.columns[3], "passenger_count") \
                   .withColumnRenamed(df.columns[7], "pulocationid") \
                   .withColumnRenamed(df.columns[8], "dolocationid") \
                   .withColumnRenamed(df.columns[16], "total_amount")

# Split into train and test DataFrames
trainDF, testDF = selected.randomSplit([0.8, 0.2], seed=42)

# Assemble features
assembler = VectorAssembler(
    inputCols=["passenger_count", "pulocationid", "dolocationid"],
    outputCol="features"
)

# Decision Tree Regressor
dt = DecisionTreeRegressor(
    featuresCol="features",
    labelCol="total_amount"
)
# Set maxBins for categorical features (IDs can be high cardinality)
dt = dt.setMaxBins(1000)

# Pipeline
pipeline = Pipeline(stages=[assembler, dt])

# Train the model
model = pipeline.fit(trainDF)

# Predict on test set
predictions = model.transform(testDF)

# Show predictions with features (first 10 entries)
print("Predictions (first 10):")
predictions.select("passenger_count", "pulocationid", "dolocationid", "total_amount", "prediction").show(10)

# Evaluate with RMSE
evaluator = RegressionEvaluator(
    labelCol="total_amount",
    predictionCol="prediction",
    metricName="rmse"
)
rmse = evaluator.evaluate(predictions)
print(f"Root Mean Squared Error (RMSE) on test data = {rmse}")

# Stop Spark session
spark.stop()
