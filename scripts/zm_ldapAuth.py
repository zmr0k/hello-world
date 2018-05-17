import requests, getpass, sys, paramiko

jiraurl = "https://jiraops.corp-apps.com/"

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

def sshoutput():
    print "\nSSHoutput: "

def sshSession(host, username, password):
  ssh = paramiko.SSHClient()
  print sshoutput(), ssh, "\n"
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh.connect(host, port=22, username=username, password=password)
  return ssh

def squareit(x):
    return x*x

# main()

#y = raw_input("Please enter any int (str): ")
#z = int(input("Please enter any int: "))
#print "Squareit of", z, "is", squareit(z)

host = "localhost"
username = "user3"
#password = getpass.getpass(prompt='Enter password for {}: '.format(username), stream=sys.stderr)
#password = "Qwerty654321"
password = getpass.win_getpass()

mysshsession = sshSession(host, username, password)
print sshoutput(), "mysshsession:", mysshsession
print "Remote server key is:", mysshsession.get_host_keys()
mysshsession.close()

#myjirasession = jiraSession(jiraurl, username, password)
#print myjirasession