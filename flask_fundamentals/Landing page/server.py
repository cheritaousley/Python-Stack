from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
  return render_template("index.html", name="Sasha")


@app.route('/ninjas')
def projects():
  return render_template('ninjas.html')


@app.route('/dojos/new')
def dojos():
   print "Got Post Info"

  #  name = request.form['name']
  #  email = request.form['email']

   return render_template('dojos.html')

app.run(debug=True)
