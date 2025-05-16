# Makefile for data processing

# Target to extract id, age, and score columns
trimmed.csv: raw.csv
	cut -d',' -f1,3,5 raw.csv > trimmed.csv

# Target to remove rows with missing values
clean.csv: trimmed.csv
	awk -F',' '(NR==1) || (779782 != "" && 779783 != "")' trimmed.csv > clean.csv

# Clean up intermediate files
clean:
	rm -f trimmed.csv clean.csv

# Default target to process all data
all: clean.csv

.PHONY: clean all
