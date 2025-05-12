#!/bin/bash
echo "adult.data entries:" $(wc -l < data/adult.data)
echo "adult.test entries:" $(wc -l < data/adult.test)
head -n 1 data/adult.data
head -n 1 data/adult.data | sed 's/,/\n/g'

# Age mean
awk -F',' '{sum+=$1} END {print "Age mean:", sum/NR}' data/adult.data

# Age median 
cut -d',' -f1 data/adult.data | sort -n > ages.txt
lines=$(wc -l < ages.txt)
lines=${lines//[[:space:]]/}
if [ $((lines % 2)) -eq 1 ]; then
  median_line=$(( (lines + 1) / 2 ))
  median=$(sed -n "${median_line}p" ages.txt)
else
  line1=$(( lines / 2 ))
  line2=$(( line1 + 1 ))
  val1=$(sed -n "${line1}p" ages.txt)
  val2=$(sed -n "${line2}p" ages.txt)
  median=$(awk "BEGIN {print ($val1+$val2)/2}")
fi
echo "Age median: $median"

