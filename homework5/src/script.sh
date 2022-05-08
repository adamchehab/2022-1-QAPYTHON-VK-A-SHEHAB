#!/bin/bash

if [ -n "$1" ]; then
	LOG_FILE="$1"
else
	LOG_FILE="../access.log"
fi

RESULTS_DIR='../results/bash/csv'

mkdir -p $RESULTS_DIR

# TASK_1 : Total requests:
awk '{print}' $LOG_FILE | wc -l | awk 'BEGIN {print "COUNT"}{print $1}' > $RESULTS_DIR/task_1.csv

# TASK_2 : Total requests by type:
awk 'length($6) < 10 {print substr($6, 2)}' $LOG_FILE | sort | uniq -c | sort -nr | awk 'BEGIN {print "TYPE COUNT"}{print $2, $1}' > $RESULTS_DIR/task_2.csv

# TASK_3 : Top 10 requests
awk '{print $7}' $LOG_FILE | sort | uniq -c | sort -nr | awk 'BEGIN {print "URL COUNT"}{print $2, $1} NR==10{exit}' > $RESULTS_DIR/task_3.csv

# TASK_4 : Top 5 biggest by size requests with 4XX error
awk '$9 ~ /^4/ {print $7, $9, length($7), $1}' $LOG_FILE | sort -r -nk3 | awk 'BEGIN {print "URL CODE SIZE IP"}{print} NR==5{exit}' > $RESULTS_DIR/task_4.csv

# TASK_5 : Top 5 users with 5XX error
awk '$9 ~ /^5/ {print $1}' $LOG_FILE | sort | uniq -c | sort -nr | awk 'BEGIN {print "IP COUNT"}{print $2, $1} NR==5{exit}'> $RESULTS_DIR/task_5.csv
