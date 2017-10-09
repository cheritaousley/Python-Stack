from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "ThisisSecret"


@app.route('/')
def index():
  print "I am gold"
  random.randrange(0, 101)
  if session.has_key('findGold') == False:
    session['findGold'] = 0
  return render_template("index.html")


@app.route('/process_money', methods=['POST'])
def guess():
    if request.form["building"] == "farm":
      session['findGold']= random.randrange(9,21)
      print request.form["buikding"]
    if request.form["building"] == "cave":
      session['findGold']= random.randrange(4,11)
      print request.form["building"]
    if request.form["building"] == "house":
      session['findGold']= random.randrange(1,6)
      print request.form["number"]
    if request.form["building"] == "casino":
      session['findGold'] = random.randrange(0, 51)
      print request.form["number"]
    return redirect('/')
  #  return redirect('/succes')


@app.route('/clear', methods=['POST'])
def clear():
   session['someKey'] = random.randrange(0, 101)
   session['message'] = " "
   return redirect('/')


app.run(debug=True)
