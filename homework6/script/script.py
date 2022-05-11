import re
import os
from collections import Counter


def repo_root():
    return os.path.abspath(os.path.join(__file__, os.pardir))


def parse_log():
    ip_adresses = []
    request_types = []
    request = []
    status_code = []

    parse_errors_dict = {}

    with open(os.path.join(repo_root(), '../access.log'), "r") as file:
        for line, string in enumerate(file, start=1):
            request_type_clean = re.sub('"', "", string.split()[5])
            if len(request_type_clean) < 10:
                ip_adresses.append(string.split()[0])
                request_types.append(request_type_clean)
                request.append(string.split()[6])
                status_code.append(string.split()[8])
            else:
                parse_errors_dict[f"line {line}"] = "Bad request method."

    request_length = {}
    for i in range(0, len(ip_adresses)):
        if status_code[i][0] == "4":
            str_combined = ip_adresses[i] + " " + request[i] + " " + status_code[i]
            request_length[str_combined] = len(request[i])

    ip_adresses_5xx_list = []
    for i in range(0, len(ip_adresses)):
        if status_code[i][0] == "5":
            ip_adresses_5xx_list.append(ip_adresses[i])

    return {
        "total_req": {f"{len(ip_adresses)}": ""},
        "req_by_type": dict(Counter(request_types)),
        "top10_req": dict(Counter(request).most_common(10)),
        "top5_req_4xx": dict(Counter(request_length).most_common(5)),
        "top5_req_5xx": dict(Counter(ip_adresses_5xx_list).most_common(5)),
    }
