#!/usr/bin/env python3

"""
Deletes indexes in ElasticSearch that are two weeks.
Example invocation:

./delete_indexes.py

Which will delete the index that is two weeks old from the day of the run.
If the current date is 2020.05.28, the index cwl-2020.05.14 or cwl-$loggroup-* will be deleted based
on env

This script is intended to run each morning as an oc cronjob.

This assumes there is NO authentication on your cluster!
"""

from datetime import date, timedelta
import sys
import requests
import os

hostname = os.environ['ES_HOSTNAME']
sre_managed = os.environ['SRE_MANAGED']
index_deleted = "index_not_found_exception"
retention_days = os.environ['RET_DAYS']
    
today = date.today()
# Note: 05.19 is the last day with data, so 06.02 is our first available window
deletable_indices = today - timedelta(days=retention_days)

index_name = ""
date_string = deletable_indices.strftime("%Y.%m.%d")

# Loaded in from the deploy template. True is a string and not a boolean value
if sre_managed == "True":
    # App sre managed indexes have the log group name in them; v3 clusters do not
    index_name = f"cwl-*-{date_string}"
else:
    index_name = f"cwl-{date_string}"

print(f"Processing delete for https://{hostname}/{index_name}")
r = requests.delete(f"https://{hostname}/{index_name}")

response_body = r.json()
if r.status_code == 200:
    print(f"Deleted index for {date_string}")
elif r.status_code == 404:
    root_cause = response_body["error"]["root_cause"][0]
    if root_cause["type"] == index_deleted:
        print("Index is already deleted")
else:
    raise ValueError("Unexpected response code: {}".format(r.status_code))

