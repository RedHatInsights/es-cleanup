#!/usr/bin/env python3

"""
Deletes indexes in ElasticSearch that are two weeks.
Example invocation:

./delete_indexes.py 

Which will delete the index that is two weeks old from the day of the run.
If the current date is 2020.05.28, the index cwl-2020.05.14 will be deleted

This script is intended to run each morning as an oc cronjob. 

This assumes there is NO authentication on your cluster!
"""

from datetime import date, timedelta
import sys
import requests
import os

hostname = os.environ['ES_HOSTNAME']

today = date.today()
two_weeks_ago = today + timedelta(days=-14)

index_name = "cwl-%s" % two_weeks_ago.strftime("%Y.%m.%d")
r = requests.delete(f"https://{hostname}/{index_name}")
if r.status_code == 200:
    print(f"Deleted index {index_name}")
else:
    raise ValueError("Bad response code: %d" % r.status_code)
