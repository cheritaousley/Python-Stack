from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
  return render_template("index.html")


@app.route('/ninja')
def ninja():  
  return render_template("ninja.html")


@app.route('/ninja/<ninja_color>')
def ninja_color(ninja_color):
    
    if ninja_color == "blue":
        return render_template("ninja_blue.html")
    elif ninja_color=="orange":
        return render_template("ninja_orange.html")
    elif ninja_color=="red":
        return render_template("ninja_red.html")
    elif ninja_color=="purple":
        return render_template("ninja_purple.html")
    else:
        return render_template("notapril.html")


app.run(debug=True)
