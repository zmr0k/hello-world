import requests, getpass, sys, paramiko

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

if __name__ == "__main__":

#y = raw_input("Please enter any int (str): ")
#z = int(input("Please enter any int: "))
#print "Squareit of", z, "is", squareit(z)

    host = "localhost"
    username = "user3"
#password = getpass.getpass(prompt='Enter password for {}: '.format(username), stream=sys.stderr)
    password = "Qwerty654321"
#    print ("Enter below your LDAP password")
#    password = getpass.win_getpass()

    mysshsession = sshSession(host, username, password)
#    print sshoutput(), "mysshsession:", mysshsession
    mysshsession.save_host_keys("C:\\users\\vklaniuk\\Host_key_from_localhost")
    mysshsession.close()
