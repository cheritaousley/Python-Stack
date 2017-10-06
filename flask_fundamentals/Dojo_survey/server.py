from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
  return render_template("index.html")


@app.route('/process', methods=['POST'])
def create_user():
   print request.form['name']
   print request.form['location']
   print request.form['language']
   print request.form['comment']
   name=request.form['name']
   location=request.form["location"]
   language=request.form['language']
   comment=request.form['comment']

   return redirect("/results/" + name + "/" + location + "/"+ language + "/" + comment ) #in real life, do not render in a post route!
#    return redirect('/process' + name + location + language + comment)


@app.route('/results/<name>/<location>/<language>/<comment>')
def results(name, location, language, comment):
  print name
  print location
  print language
  print comment
  return render_template("results.html", name=name, location=location ,language=language , comment=comment)


app.run(debug=True)
