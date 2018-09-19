#!/usr/bin/env python

import cgi, cgitb
import os
cgitb.enable()

form = cgi.FieldStorage()

returns_name = form.getvalue('Name')
returns_order = form.getvalue('order_number')
returns_reason = form.getvalue('Reason')
returns_action = form.getvalue('Action')

   
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Hello - Second CGI Program</title>"
print "</head>"
print "<body>"
print "<h1 style='font-size:300%;'>Details for Return<h1>"
print "<br>"
print "<h2>Name: %s</h2>" % (returns_name)
print "<h2>Order Number: %s</h2>" % (returns_order)
print "<h2>Reason: %s</h2>" % (returns_reason)
print "<h2>Action: %s</h2>" % (returns_action)
print "</body>"
print "</html>"

def send_message_to_slack(name, order, reason, action):
    import urllib2
    import json
    
    return_details = "Over The Counter Returns:" + "\n" + "--------------------------------" + "\n\n" + "Full Name " + name + "\n" + "Order number: " + order + "\n\n" + "Reason: " + reason + "\n" + "Action: " + action
    post = {"text": "{0}".format(return_details)}

    try:
        json_data = json.dumps(post)
        req = urllib2.Request("https://hooks.slack.com/services/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",
                              data=json_data.encode('ascii'),
                              headers={'Content-Type': 'application/json'}) 
        resp = urllib2.urlopen(req)
    except Exception as em:
        print("EXCEPTION: " + str(em))
        
send_message_to_slack(returns_name, returns_order, returns_reason,returns_action)'''