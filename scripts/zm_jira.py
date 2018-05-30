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

    #try:
    #    projects_list = jira.projects()
    #    for i in projects_list:
    #        print i
    #except:
    #    print "Error: Exception on projects list."

    myito = "ITO-98297"
    issue = jira.issue(myito)
    print issue
    print issue.fields

    text = "Just text for comment"
    try:
        comment_issue = jira.add_comment(myito, text)
    except:
        print "Error putting comment"
        exit(-1)

    assignee = jira.assign_issue(myito, jiralogin)
    #jira.close()

    #print "Fileds:", issue.fields()
    #for issue_field_name in issue.raw['fields']:
    #    print "Field name: [", issue_field_name, "] // Value:", issue.raw['fields'][issue_field_name]


    #print "Should be fields:", issue.raw['fields']
    #['issuetype']

    issue_dict = {
        'project': {'name': 'IT Operations'},
        'summary': 'zm-Savage-Test',
        'description': 'zm_savage-test',
        'issuetype': {'name': 'ITO-Support'},
        #'customfield_11107': 'Not Applicable'
    }

    #try:
    create_issue = jira.create_issue(fields=issue_dict)
    #except:
    #    print "Exception: issue wasn't created"
#    jira.assign_issue(jiralogin)
#    jira.close()

    #issues_in_inc = jira.search_issues('project=INC')
    #print issues_in_inc

