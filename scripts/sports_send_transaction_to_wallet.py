#!/usr/bin/python
import urllib2
import json
import requests
from requests.auth import HTTPBasicAuth

url = "http://sports-backend-api-bet.b2pa.internal/abp/rest/transactions/bet/%s"
settle = "http://sports-backend-api-bet.b2pa.internal/abp/rest/outcomes/%s/settle"

transactions_file = open("transactions2.txt", "r+")

transactions = transactions_file.readlines()
i = 0
for transaction in transactions:
    i += 1
    print "%s/%s - %s" % (i, len(transactions), transaction.strip("\n\t\r"))
    req = urllib2.Request(url % transaction, headers={"Authorization": "Basic YmdzLWJjZy1tZGV2OiE0b0lsaW1Y"})
    res = urllib2.urlopen(req)

    out = json.loads(res.read())
    tx = out['transactions'][0]
    if tx["status"] != "SETTLED":
        print "%s,%s" % (transaction.strip("\n\t\r"), tx["status"])
        outcomes = []
        for betData in tx['betDataList']:
            outcomes.append(str(betData['outcomeId']))
        outcomeList = ','.join(outcomes)
        print settle % outcomeList
        r = requests.put(
            settle % (outcomeList),
            auth=HTTPBasicAuth("bgs-bcg-test", "uruiIEU2JDj"))
        if r.status_code != 204:
            print 'Please check this one!'
