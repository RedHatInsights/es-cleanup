#!/usr/bin/env python3

"""
Deletes indexes in ElasticSearch that are older than one week.
Example invocation:

./delete_indexes.py my-cluster.us-east-1.es.amazonaws.com 2019.07.01

Which will delete all the indexes starting with cwl-2019.07.01 until the index
that is one week old

This assumes there is NO authentication on your cluster!
"""

from datetime import date, timedelta
import sys
import requests
import os

"""
this dude needs a couple things:
1. Either a passed in date of the current cron job (2020.05.25) or just grab the current date from the api
2. A hostname to be pointed at (could split to 2 jobs or just do both with one)

"""

if len(sys.argv) < 3:
    print("provide server hostname and index start date YYYY.mm.dd")
    sys.exit(0)

hostname = os.environ['ES_HOSTNAME']
print(f"going to {hostname}")

today = date.today()
two_weeks_ago = today + timedelta(days=-14)

# index_date = date(**dict(zip(["year", "month", "day"], [int(i) for i in start_date.split(".")])))

index_name = "cwl-%s" % two_weeks_ago.strftime("%Y.%m.%d")
# r = requests.delete(f"https://{hostname}/{index_name}")
# if r.status_code == 200:
print(f"Deleted index {index_name}, but not really ;0")
# else:
#     raise ValueError("Bad response code: %d" % r.status_code)

# index_date = index_date + timedelta(days=1)