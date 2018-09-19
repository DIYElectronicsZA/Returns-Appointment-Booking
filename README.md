#Returns-Appointment-Booking

**An Internal automated bookings system that captures users data and posts to a slack channel via a python scrpit.**  

###Info

User info is entered into a static HTML page which posts values submitted to a python script.  
The python script then in turn uses a service key provided through Slack Webhooks to post the formatted information into a channel.

###Requirements

Apache2
Python27
[Enable cgi for running python scripts](https://www.linux.com/blog/configuring-apache2-run-python-scripts) 
