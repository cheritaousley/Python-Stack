from flask import Flask, render_template, redirect, request, flash
import re
from mysqlconnection import MySQLConnector
import datetime
app = Flask(__name__)

mysql = MySQLConnector(app, 'email_db')

print mysql.query_db("SELECT * FROM email")
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"


@app.route('/', methods=['GET'])
def index():
    print mysql.query_db("SELECT * FROM email")
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def submit():
    errors= [ ]
    email = request.form['email']
    existing_email=mysql.query_db("SELECT * FROM email WHERE email_address ='{}' ".format(email))
    if len(existing_email) > 0:
        # flash("Email already exists")
        errors.append("Email already exists")
    if len(request.form['email']) < 1:
        # flash("Email cannot be blank!")
        errors.append("Email cannot be blank!")
    if len(errors)>0:
        flash(errors)
    else:
        flash("Success! Your email address is {}".format(request.form['email']))
        mysql.query_db( "INSERT INTO email (email_address) VALUES ('{}')".format(email))
    print email
    return redirect('/success')

@app.route('/success')
def success():
    print mysql.query_db("SELECT * FROM email")
    email = mysql.query_db("SELECT * FROM email")
    # flash("Success!")
    return render_template("success.html", email=email)

app.run(debug=True)
