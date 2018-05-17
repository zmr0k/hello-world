import requests, getpass, sys, pytz

def jiraSession(jiraurl, username, password):
  # Generate jira session cookies
  url = '{}/rest/gadget/1.0/login'.format(jiraurl)
  try:
    req = requests.post(url, auth=(username, password))
    print "Req is:", req
    try:
      auth = req.cookies['atlassian.xsrf.token']
    except:
      print 'Jira authentication failed, please check your password'
      exit(1)
    return req.cookies
  except requests.exceptions.RequestException as e:
    print 'Error: {}\n{}'.format(e, req.text)
    return

def jiraJqlIssues(jiraurl, jirasession, query):
  # Find jira issues from JQL query
  print 'Finding issues using query: {}'.format(query)
  url = '{}/rest/api/2/search'.format(jiraurl)
  data = {
    'jql': query,
    'startAt': 0,
    'maxResults': 20,
    'fields': ['summary', 'status', 'assignee']
  }
  try:
    req = requests.get(url, params=data, cookies=jirasession)
    return req.json()['issues']
  except requests.exceptions.RequestException as e:
    logger.error('{} {}'.format(e, req.text))


if __name__ == "__main__":

#y = raw_input("Please enter any int (str): ")
#z = int(input("Please enter any int: "))
#print "Squareit of", z, "is", squareit(z)
#    host = "localhost"
#password = getpass.getpass(prompt='Enter password for {}: '.format(username), stream=sys.stderr)
#    password = "Qwerty654321"
#    print ("Enter below your LDAP password")

    jiraurl = "https://jiraops.mdev.corp-apps.com"

    r = requests.get(jiraurl)
    if r.status_code == 200 or r.status_code == 304:
        print "Status code:", r.status_code
    # we dont want to get a page
    #    print "Text:", r.text
        print "Header:", r.headers
        print "Cookies", r.cookies

    else:
        print "Status code", r.status_code, "is not 200"
        exit(-1)


    username = getpass.getuser()
    print "Using user [", username, "] for current JIRA session"
    password = getpass.win_getpass()

    myjirasession = jiraSession(jiraurl, username, password)
    print myjirasession

# Search for existing issues
    issues = jiraJqlIssues(jiraurl, myjirasession, 'Can i create')
    print issues