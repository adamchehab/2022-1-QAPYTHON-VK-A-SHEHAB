import re
import os
import argparse
from collections import Counter

from utils import create_folder
from utils import make_csv
from utils import csv_to_json


# Settings
CSV_RESULTS_DIR = "../results/python/csv"
JSON_RESULTS_DIR = "../results/python/json"


# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("--json", action="store_true")
parser.add_argument("--log_path", default="../access.log")
flags = parser.parse_args()


# Parse LOG file and add data to lists:
ip_adresses = []
request_types = []
request = []
status_code = []
parse_errors_dict = {}
with open(flags.log_path, "r") as file:
    for line, string in enumerate(file, start=1):
        request_type_clean = re.sub('"', "", string.split()[5])
        if len(request_type_clean) < 10:
            ip_adresses.append(string.split()[0])
            request_types.append(request_type_clean)

            # Request URL - URL/URI (get path from URI + remove params (? #))
            value = re.split(r"[?#]", string.split()[6])[0]
            if "http://" in value:
                val = "/" + "/".join(value.split("/")[3:])
            request.append(val)

            status_code.append(string.split()[8])
        else:
            parse_errors_dict[f"line {line}"] = "Bad request method."


# Create results/csv folder if it doesnt exist
create_folder(CSV_RESULTS_DIR)


# TASK_1 : Total requests:
make_csv(filename=f"{CSV_RESULTS_DIR}/task_1", data={f"{len(ip_adresses)}": ""}, headers=["TOTAL"])


# TASK_2 : Total requests by type:
make_csv(filename=f"{CSV_RESULTS_DIR}/task_2", data=Counter(request_types), headers=["TYPE", "COUNT"])


# TASK_3 : Top 10 requests
make_csv(filename=f"{CSV_RESULTS_DIR}/task_3", data=dict(Counter(request).most_common(10)), headers=["REQUEST", "COUNT"])


# TASK_4 : Top 5 biggest by size requests with 4XX error
# Prepare dictionary for TASK_4
request_length = {}
for i in range(0, len(ip_adresses)):
    if status_code[i][0] == "4":
        str_combined = ip_adresses[i] + " " + request[i] + " " + status_code[i]
        request_length[str_combined] = len(request[i])

make_csv(
    filename=f"{CSV_RESULTS_DIR}/task_4",
    data=dict(Counter(request_length).most_common(5)),
    headers=["IP", "URL", "CODE", "LEN"],
)


# TASK_5 : Top 5 users with 5XX error
# Prepare list for TASK_5
ip_adresses_5xx_list = []
for i in range(0, len(ip_adresses)):
    if status_code[i][0] == "5":
        ip_adresses_5xx_list.append(ip_adresses[i])

make_csv(
    filename=f"{CSV_RESULTS_DIR}/task_5",
    data=dict(Counter(ip_adresses_5xx_list).most_common(5)),
    headers=["IP", "COUNT"],
)


# Convert CSV to JSON - Check JSON flag and then convert JSON to DICT
if flags.json:
    # Create results/json folder if it doesnt exist
    create_folder(JSON_RESULTS_DIR)
    # Get list of CSV result files names
    csv_result_files = os.listdir(CSV_RESULTS_DIR)
    # Convert CSV files to JSON files
    for i in range(0, len(csv_result_files)):
        csv_to_json(f"{CSV_RESULTS_DIR}/{csv_result_files[i]}", f"{JSON_RESULTS_DIR}/{csv_result_files[i].split('.')[0]}.json")
