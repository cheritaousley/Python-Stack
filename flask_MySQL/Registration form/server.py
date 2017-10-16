from flask import Flask, render_template, request, redirect, session, flash
import re
from mysqlconnection import MySQLConnector
import datetime
import md5  
# import os, binascii
password = 'password'
hashed_password = md5.new(password).hexdigest()
print hashed_password  

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisisSecret"


mysql = MySQLConnector(app, 'mydb')

print mysql.query_db("SELECT * FROM registers")


@app.route('/', methods=['GET'])
def index():
    print mysql.query_db("SELECT * FROM registers")
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
    password= request.form['password']
    created_at=request.form['created_at']
    updated_at=request.form['updated_at']
    password = md5.new(request.form['password']).hexdigest()
    # password= md5.new(password).hexdigest()
    # salt = binascii.b2a_hex(os.urandom(15))
    # hashed_password = md5.new(password + salt).hexdigest()
    confirm_password = request.form['confirm_password']
    existing_email = mysql.query_db("SELECT * FROM registers WHERE email ='{}' ".format(email))

    if len(existing_email) > 0:
        errors.append("Email already exists")
        return redirect('/login')
    if len(request.form['first_name']) < 1:
        errors.append("Name cannot be empty!")
    else:
      flash("Success! Your first name is {}".format(request.form['first_name']))
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
    else:
        flash("Success! Your email address is {}".format(request.form['email']))
    if len(request.form['password'])< 1:
        errors.append("Password should be more than 8 characters")
    else:
        flash("Success!")
    if len(request.form['confirm_password']) < 1:
        errors.append("Password should be more than 8 characters")
    else:
        flash("Success!")
    if request.form['password'] != request.form['confirm_password']:
        errors.append("Confirm password and password do not match")
    else:
        flash("Success!")
    if len(errors) > 0:
        flash(errors)
    else:
        flash("Success!")
        mysql.query_db("INSERT INTO registers (first_name, last_name, email, password, created_at, updated_at) VALUES ('{}','{}','{}','{}', '{}', '{}')".format(first_name, last_name, email, password, created_at, updated_at))
        return redirect('/success')
    return redirect ('/')

@app.route('/success')
def success():
    print mysql.query_db("SELECT * FROM registers")
    first_name = mysql.query_db("SELECT * FROM registers")
    last_name = mysql.query_db("SELECT * FROM registers")
    email = mysql.query_db("SELECT * FROM registers")
    password = mysql.query_db("SELECT * FROM registers")
    # flash("Success!")
    return render_template("success.html", first_name=first_name, last_name=last_name, email=email, password=password)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    # else:             #this logic coudl be done in this route without making a new route(/signin), but to me, it's a much cleaner style to create seperate routes
        # email = request.form["email"]
        # password = request.form['password']
        # users = mysql.query_db("SELECT * FROM registers WHERE email ='{}' ".format(email))
        # if len(users)>0:
        #     user = users[0]
        #     if user.password== password:
        #         print "Successful login!"
        # else:
        #     print "no such user!"
@app.route('/signin', methods=['POST'])
def signin():
    email = request.form["email"]
    password = request.form['password']
    # session['first_name'] = request.form['first_name']
    # session['last_name']=request.form['last_name']
    # session['email']=request.form['email']
    users = mysql.query_db("SELECT * FROM registers WHERE email ='{}' ".format(email))
    if len(users) > 0:
        user = users[0]
        if user['password'] == password:
            print "Successful login!"
            session['first_name']=user['first_name']
            session['email']= user['email']
    else:
        print "no such user!"
    return redirect("/successfullogin")

@app.route('/successfullogin') #you should never render in a POST route ! you should only redirct it to the "successful" route. POST routes are used to process the information 
def successful_login():
    return render_template("signedIn.html")

@app.route('/logout', methods=['POST'])
def logout():
    flash("You are logged out")
    return redirect('/login')

app.run(debug=True)
