from jira import JIRA
import getpass

jiralogin = "vklaniuk"
jirapass = getpass.win_getpass()

options = {
    'server': "https://jiraops.mdev.corp-apps.com",
#    'auth': "jiralogin", "jirapasss"

}

jira = JIRA(options, auth=(jiralogin, jirapass))


print "Jira object is [", jira, "]"

projects_list = jira.projects()
print projects_list

issue = jira.issue("ITO-98297")
print issue

update_issue = jira._check_update_()