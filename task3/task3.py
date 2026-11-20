import sys
import json


values_file, tests_file, report_file = sys.argv[1:4]

with open(values_file, encoding="utf-8") as file:
    values = json.load(file)

with open(tests_file, encoding="utf-8") as file:
    tests = json.load(file)

results = {item["id"]: item["value"] for item in values["values"]}


def fill_values(items):
    for item in items:
        if item["id"] in results:
            item["value"] = results[item["id"]]

        if "values" in item:
            fill_values(item["values"])


fill_values(tests["tests"])

with open(report_file, "w", encoding="utf-8") as file:
    json.dump(tests, file, ensure_ascii=False, indent=2)