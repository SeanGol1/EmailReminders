#from idna import unicode
from newsapi import NewsApiClient
import json
from datetime import date, timedelta
import smtplib, ssl
from configparser import ConfigParser

# Set up 
configfile = 'config.ini'
config = ConfigParser()
config.read(configfile)
newsapi = NewsApiClient(api_key=config['api']['api_key'])
todaydate = date.today()
yestdate = todaydate - timedelta(days=1)
emailstr = ""


# Top Tech headlines
tech_headlines = newsapi.get_top_headlines(sources='mashable,techcrunch.com')

# Top Irish headlines    
irish_headlines = newsapi.get_top_headlines(country='ie')



########  Irish Headlines
emailstr += "Irish Headlines - "
emailstr += str(irish_headlines['totalResults'])
emailstr += " Stories\r\n\r\n"
for items in irish_headlines:
    if(items == 'articles'):
        for articles in irish_headlines[items]:
            emailstr += articles['title']
            emailstr += "\r\n\r\n"
            emailstr += articles['content']
            emailstr += "\r\n"
            emailstr += articles['url']
            emailstr += "\r\n___________________________________________________________________________________\r\n"


########  Tech Headlines
emailstr += "======================================================================================\r\n\r\n"
emailstr += "Tech Headlines - "
emailstr += str(tech_headlines['totalResults'])
emailstr += " Stories\r\n\r\n"
for items in tech_headlines:
     if(items == 'articles'):
         for articles in tech_headlines[items]:
             emailstr += articles['title']
             emailstr += "\r\n"
             emailstr += articles['content']
             emailstr += "\r\n"
             emailstr += articles['url']
             emailstr += "\r\n_______________________________\r\n"


# Take from config file
sender_email = config['email']['sender_email']
sender_password = config['email']['sender_password']
sender_email_port = config['email']['sender_email_port']
receiver_email = config['email']['receiver_email']

# Set up a default heading for the email
message = """\
Subject: News Headlines 

"""

message += emailstr

port = 587  # For starttls
context = ssl.create_default_context()
with smtplib.SMTP(sender_email_port, port) as server:
     server.ehlo()  
     server.starttls(context=context)
     server.ehlo()  
     server.login(sender_email, sender_password)
     server.sendmail(sender_email, receiver_email, message.encode("utf-8"))

