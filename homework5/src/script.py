import csv
import json
import os


# Settings
CSV_RESULTS_DIR = "../results/csv"
JSON_RESULTS_DIR = "../results/json"


# Write CSV to JSON file
def csv_to_json(csvFilePath, jsonFilePath):
    data = []
    with open(csvFilePath) as csvf:
        csvReader = csv.DictReader(csvf, delimiter=" ")
        for row in csvReader:
            data.append(row)
    with open(jsonFilePath, "w") as jsonf:
        jsonString = json.dumps(data, indent=4)
        jsonf.write(jsonString)


# List of CSV result files
csv_result_files = os.listdir(CSV_RESULTS_DIR)


# Convert CSV files to JSON files
for i in range(0, len(csv_result_files)):
    csv_to_json(f"{CSV_RESULTS_DIR}/{csv_result_files[i]}", f"{JSON_RESULTS_DIR}/{csv_result_files[i].split('.')[0]}.json")
