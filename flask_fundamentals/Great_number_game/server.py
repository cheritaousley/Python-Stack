from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "ThisisSecret"


@app.route('/')
def index():
  print "I am a number"
  random.randrange(0, 101)
  if session.has_key('someKey') == False:
    session['someKey']= random.randrange(0, 101)
    print session["someKey"]
  # session.pop('someKey')
  return render_template("index.html")


@app.route('/guess', methods=['POST'])
def guess():
  print "processing the guess!"
  if int(request.form["number"]) < session['someKey']:
     session['message']= 'Too Low'
     session["status"] = "wrong"
     print "too low"
     print request.form["number"]
     print session["someKey"]
  if int(request.form["number"]) > session['someKey']:
     session['message'] = 'Too High'
     session["status"] = "wrong"
     print "Too high"
     print request.form["number"]
     print session["someKey"]
  if int(request.form["number"]) == session["someKey"]:
     session["message"] = "You're the REAL MVP"
     session["status"] = "right"
     print request.form["number"]
     print session["someKey"]
  return redirect('/')
  #  return redirect('/succes')


@app.route('/clear', methods=['POST'])
def clear():
   session['someKey'] = random.randrange(0,101)
   session['message'] = " "
   return redirect('/')


app.run(debug=True)
