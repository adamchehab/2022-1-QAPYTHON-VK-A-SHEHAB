import os
import csv
import json


# Create folder if it doesnt exist
def create_folder(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


# Procedure - write dictionary (data) to CSV file
def make_csv(filename, data, headers=None):
    with open(filename + ".csv", "w", newline="") as file:
        writer = csv.writer(file, delimiter=" ")
        if headers:
            writer.writerow(headers)
        for key in data:
            row = key.split()
            if data[key] != "":
                row.append(data[key])
            writer.writerow(row)


# Procedure - Write CSV to JSON file
def csv_to_json(csvFilePath, jsonFilePath):
    data = []
    with open(csvFilePath) as csvf:
        csvReader = csv.DictReader(csvf, delimiter=" ")
        for row in csvReader:
            data.append(row)
    with open(jsonFilePath, "w") as jsonf:
        jsonString = json.dumps(data, indent=4)
        jsonf.write(jsonString)
