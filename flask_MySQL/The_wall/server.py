from flask import Flask, render_template, request, redirect, session, flash
import re
from mysqlconnection import MySQLConnector
import datetime
import md5
import os, binascii
password = 'password'
hashed_password = md5.new(password).hexdigest()
print hashed_password

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisisSecret"


mysql = MySQLConnector(app, 'mydb')

print mysql.query_db("SELECT * FROM users")


@app.route('/')
def index():
    print mysql.query_db("SELECT * FROM users")
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def create_user():
    print request.form['first_name']
    print request.form['last_name']
    print request.form['email']
    print request.form['password']
    print request.form['confirm_password']
    errors = []
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form["email"]
    password = request.form['password']
    password = md5.new(request.form['password']).hexdigest()
    # salt = binascii.b2a_hex(os.urandom(15))
    # hashed_password = password + salt
    confirm_password = request.form['confirm_password']
    existing_email = mysql.query_db("SELECT * FROM users WHERE email ='{}' ".format(email))

    if len(existing_email) > 0:
        errors.append("Email already exists")
        return redirect('/login')
    if len(request.form['first_name']) < 1:
        errors.append("Name cannot be empty!")
    else:
      flash("Success! Your first name is {}".format(
          request.form['first_name']))
    if len(request.form['first_name']) > 1 and request.form["first_name"].isdigit():
        errors.append("Name cannot contain numbers")
    if len(request.form['last_name']) < 1:
        errors.append("Name cannot be empty!")
    else:
      flash("Success! Your last name is {}".format(request.form['last_name']))
    if len(request.form['first_name']) > 1 and request.form["first_name"].isdigit():
        errors.append("Name cannot contain numbers")
    if len(request.form['email']) < 1:
        errors.append("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        errors.append("Invalid Email Address!")
    # else:
    #     flash("Success! Your email address is {}".format(
    #         request.form['email']))
    if len(request.form['password']) < 1:
        errors.append("Password should be more than 8 characters")
    # else:
    #     flash("Success!")
    if len(request.form['confirm_password']) < 1:
        errors.append("Password should be more than 8 characters")
    # else:
    #     flash("Success!")
    if request.form['password'] != request.form['confirm_password']:
        errors.append("Confirm password and password do not match")
    # else:
    #     flash("Success!")
    if len(errors) > 0:
        flash(errors)
    else:
        flash("Success!")
        mysql.query_db("INSERT INTO users (first_name, last_name, email, password) VALUES ('{}','{}','{}','{}')".format(first_name, last_name, email, password))
        return redirect('/success')
    return redirect('/')


@app.route('/success')
def success():
    print mysql.query_db("SELECT * FROM users")
    first_name = mysql.query_db("SELECT * FROM users")
    last_name = mysql.query_db("SELECT * FROM users")
    # email = mysql.query_db("SELECT * FROM users")
    # password = mysql.query_db("SELECT * FROM users")
    return render_template("success.html", first_name=first_name, last_name=last_name)

@app.route('/login')
def login():
        return render_template("login.html")
  


@app.route('/signin', methods=['POST'])
def signin():
    email = request.form["email"]
    password = request.form['password']
    password = md5.new(request.form['password']).hexdigest()
    existing_users = mysql.query_db("SELECT * FROM users WHERE email ='{}' ".format(email))
    print existing_users[0]['password']
    stored_password = mysql.query_db("SELECT password FROM users WHERE email ='{}' ".format(email))
    if len(existing_users) > 0:
        user = existing_users[0]
    else:
        flash("No such user")
        return redirect ('/')
    if password == existing_users[0]['password']:
        print "successful login"
        session['users_id']=user['id']
        return redirect("/thewall")
    else:
        return redirect('/')

@app.route('/thewall')
def successful_login():
    users = mysql.query_db("SELECT * FROM users")
    messages = mysql.query_db("SELECT * FROM messages")
    comments = mysql.query_db("SELECT * FROM comments")
    print messages
    print mysql.query_db("SELECT * FROM messages")
    print mysql.query_db("SELECT * FROM comments")
    
    return render_template("thewall.html", messages=messages, comments=comments, users=users)

@app.route('/createmessage', methods=['POST'])
def create_message():
    # session['message']= message['message']
    user_id= session['users_id']
    message = request.form['message']
    created_at=datetime.datetime.now()
    mysql.query_db("INSERT INTO messages (users_id, message, created_at) VALUES ({},'{}','{}')".format(user_id, message, created_at))
    return redirect ('/thewall')


@app.route('/createcomment', methods=['POST'])
def create_comments():
    comment = request.form['comment']
    user_id = session['users_id']
    message_id= request.form['message_id']
    created_at = datetime.datetime.now()
    mysql.query_db("INSERT INTO comments (messages_id, users_id, comment, created_at) VALUES ({},{},'{}','{}')".format(
        message_id, user_id, comment, created_at))
    return redirect('/thewall')

@app.route('/logout', methods=['POST'])
def logout():
    flash("You are logged out")
    return redirect('/login')


app.run(debug=True)
