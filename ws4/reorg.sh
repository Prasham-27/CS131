# Get current date/time info
datetime=$(date "+%F-%T")

# Vendor IDs to process
vendorids=("1.0" "2.0" "4.0")

# Add generated CSV files to .gitignore
for vendor in "${vendorids[@]}"
do
    echo "${datetime}-${vendor}.csv" >> .gitignore
done

# Loop through all 2019 taxi dataset files and reorganize by vendorid
for file in 2019-*.csv
do
    for vendor in "${vendorids[@]}"
    do
        # Extract header line only once per output file (if file doesn't exist yet)
        if [ ! -f "${datetime}-${vendor}.csv" ]; then
            head -n 1 "$file" > "${datetime}-${vendor}.csv"
        fi

        # Append lines matching vendorid to corresponding CSV file
        awk -F, -v vendor="$vendor" 'NR>1 && $1==vendor' "$file" >> "${datetime}-${vendor}.csv"
    done
done

# Create ws4.txt with wc results for each CSV file
> ws4.txt  # Clear ws4.txt if exists

for vendor in "${vendorids[@]}"
do
    wc "${datetime}-${vendor}.csv" >> ws4.txt
done

# Append contents of .gitignore to ws4.txt
echo -e "\nContents of .gitignore:" >> ws4.txt
cat .gitignore >> ws4.txt
