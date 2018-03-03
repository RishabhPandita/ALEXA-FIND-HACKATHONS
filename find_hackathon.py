import logging
import MySQLdb
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)
db = MySQLdb.connect(host="webscrapper-instance.c2ay3hczfmtj.us-east-2.rds.amazonaws.com", 
			user="admin_webscrap", 
			passwd="password", 
			db="mlh_data")

cur = db.cursor()


@ask.launch
def start_app():
    
    print('Inside application')
    welcome_msg = render_template('welcome')
    ready = render_template('ready')
    reprompt = render_template('reprompt')
    print('New welcome message is::::  ' , welcome_msg)
    return question(ready).reprompt(reprompt)



