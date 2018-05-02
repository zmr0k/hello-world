import requests

url = "https://jiraops.corp-apps.com/"
r = requests.get(url)

if r.status_code == 200:
    print "Status code:", r.status_code
    print "2Status code:", r.status_code
else:
    print "Status code", r.status_code, "is not 200"