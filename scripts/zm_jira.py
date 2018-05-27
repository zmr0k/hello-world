from jira import JIRA
import getpass

if __name__ == "__main__":

    jiralogin = "vklaniuk"
    jirapass = getpass.win_getpass()

    options = {
        'server': "https://jiraops.mdev.corp-apps.com",
    #    'auth': "jiralogin", "jirapasss"
    }

    try:
        jira = JIRA(options, auth=(jiralogin, jirapass))
        print "Jira object is [", jira, "]"
    except:
        print "\nJira auth failed. No session was created\n"

    try:
        projects_list = jira.projects()
        for i in projects_list:
            print i
    except:
        print "Error: Exception on projects list."

    myito = "ITO-98297"
    issue = jira.issue(myito)
    print issue

    text = "Just text for comment"
    try:
        comment_issue = jira.add_comment(myito, text)
    except:
        print "Error putting comment"
        exit(-1)

    assignee = jira.assign_issue(myito, jiralogin)
    jira.close()

    #create_issue = jira.create_issue(project="INC", summary="Creating issue with python", description="Description: Creating issue with python")
#    jira.assign_issue(jiralogin)
#    jira.close()

    issues_in_inc = jira.search_issues(project="INC")
    print issues_in_inc
