#!/bin/bash

LOG_FILE="$1"
RESULTS_DIR='results/csv'

mkdir -p $RESULTS_DIR

# Task 1 : Total requests:
awk '{print}' $LOG_FILE | wc -l | awk 'BEGIN {print "COUNT"}{print $1}' > $RESULTS_DIR/TASK1-total_requests.csv

# Task 2 : Total requests by type:
awk 'length($6) < 10 {print substr($6, 2)}' $LOG_FILE | sort | uniq -c | sort -nr | awk 'BEGIN {print "TYPE COUNT"}{print $2, $1}' > $RESULTS_DIR/TASK2-total_requests_by_type.csv

# Task 3 : Top 10 requests
awk '{print $7}' $LOG_FILE | sort | uniq -c | sort -nr | awk 'BEGIN {print "URL COUNT"}{print $2, $1} NR==10{exit}' > $RESULTS_DIR/TASK3-top_10_requests.csv

# Task 4 : Top 5 biggest by size requests with 4XX error
awk '$9 ~ /^4/ {print $7, $9, length($7), $1}' $LOG_FILE | sort -r -nk3 | awk 'BEGIN {print "URL CODE SIZE IP"}{print} NR==5{exit}' > $RESULTS_DIR/TASK4-top_5_requests_with_4XX.csv

# Task 5 : Top 5 users with 5XX error
awk '$9 ~ /^5/ {print $1}' $LOG_FILE | sort | uniq -c | sort -nr | awk 'BEGIN {print "IP COUNT"}{print $2, $1} NR==5{exit}'> $RESULTS_DIR/TASK5-top_5_requests_with_5XX.csv