#!/usr/bin/awk -f

# Function to calculate average from a sum and count
function calculate_average(sum, count) {
    return sum / count
}

BEGIN {
    FS = ","  # Set field separator to comma for CSV
    print "Student Grade Analysis"
    print "======================"
    
    # Initialize variables to track highest and lowest scores
    highest_score = -1
    lowest_score = 999999
    highest_student = ""
    lowest_student = ""
}

# Skip the header row
NR == 1 {
    # Store the number of grade columns (total fields minus 2 for ID and Name)
    num_grade_columns = NF - 2
    next
}

# Process each student record
{
    student_id = $1
    student_name = $2
    
    # Calculate sum of grades for current student
    sum = 0
    for (i = 3; i <= NF; i++) {
        sum += $i
    }
    
    # Store sum in associative array
    student_sum[student_id] = sum
    
    # Calculate average using the function
    avg = calculate_average(sum, num_grade_columns)
    student_avg[student_id] = avg
    
    # Determine pass/fail status
    if (avg >= 70) {
        status = "Pass"
    } else {
        status = "Fail"
    }
    student_status[student_id] = status
    
    # Store student name for later use
    student_names[student_id] = student_name
    
    # Track highest and lowest scoring students
    if (sum > highest_score) {
        highest_score = sum
        highest_student = student_id
    }
    
    if (sum < lowest_score) {
        lowest_score = sum
        lowest_student = student_id
    }
}

END {
    print "\nStudent Results:"
    print "---------------"
    
    # Print details for each student
    for (id in student_sum) {
        print "Student: " student_names[id]
        print "Total Score: " student_sum[id]
        print "Average Score: " student_avg[id]
        print "Status: " student_status[id]
        print ""
    }
    
    # Print highest and lowest scoring students
    print "Top Scoring Student: " student_names[highest_student] " (Total: " highest_score ")"
    print "Lowest Scoring Student: " student_names[lowest_student] " (Total: " lowest_score ")"
}

