from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisisSecret"

@app.route('/')
def index():
  if session.has_key('count')== False:      #the has_key() was the main take away from this assignment ans using sessions. We first checked to see if sessions had a key 'count", if it DOES NOT then
    session['count'] = 0
    # session['count']+= 1
  # else:
  #   # session['count'] += 1
   
  return render_template("index.html", count = session['count'])


@app.route('/increment', methods=['POST'])
def increment():

   session['count'] += 2
   return redirect ('/')


@app.route('/clear', methods=['POST'])
def clear():
   session['count']= 0
   return redirect('/')

app.run(debug=True)
