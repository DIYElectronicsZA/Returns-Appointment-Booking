#!/usr/bin/env python

import cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()

returns_name = form.getvalue('Name')
returns_email = form.getvalue('Email')
returns_contact = form.getvalue('Contact')
returns_order = form.getvalue('order_number')
returns_reason = form.getvalue('Reason')
returns_action = form.getvalue('Action')
returns_ticket = form.getvalue('ticket_number')

print("Content-Type: text/html;charset=utf-8")   
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Hello - Second CGI Program</title>"
print "</head>"
print "<body>"
print "<h1 style='font-size:300%;'>Details for Return<h1>"
print "<br>"
print "<h2>Name: %s</h2>" % (returns_name)
print "<h2>Email: %s</h2>" % (returns_email)
print "<h2>Contact Number: %s</h2>" % (returns_contact)
print "<h2>Order Number: %s</h2>" % (returns_order)
print "<h2>Ticket Number: %s</h2>" % (returns_ticket)
print "<h2>Reason: %s</h2>" % (returns_reason)
print "<h2>Action: %s</h2>" % (returns_action)
print "</body>"
print "</html>"

def send_message_to_slack(name, email, contact, order, ticket, reason, action):
    import urllib2
    import json
    
    if name is None:
        name = "NA"
    if order is None:
        order = "NA"
    if email is None:
        email = "NA"
    if contact is None:
        contact = "NA"
    if ticket is None:
        ticket = "NA"
    if reason is None:
        reason = "NA"
    if action is None:
        action = "NA"
        
    return_details = "Over The Counter Returns:" + "\n" + "--------------------------------" + "\n\n" + "Full Name " + name + "\n" + "Email: " + email + "\n" + "Contact Number: " + contact + "\n" + "Order number: " + order + "\n" + "Ticket Number: " + ticket + "\n\n" + "Reason: " + reason + "\n" + "Action: " + action
    post = {"text": "{0}".format(return_details)}

    try:
        json_data = json.dumps(post)
        req = urllib2.Request("x",
                              data=json_data.encode('ascii'),
                              headers={'Content-Type': 'application/json'}) 
        resp = urllib2.urlopen(req)
    except Exception as em:
        print("EXCEPTION: " + str(em))
        
send_message_to_slack(returns_name, returns_email, returns_contact, returns_order, returns_ticket, returns_reason,returns_action)