from flask import Flask  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
@app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
                         # function to the '/' route. This means that whenever we send a request to
                         # localhost:5000/ we will run the following "hello_world" function.
def hello_world():
  return 'Hello World!'  # Return the string 'Hello World!' as a response.


@app.route('/show me the cats')
def show_me_the_cats():         #try to name the function the same thing as the route before it
  return 'Here are the dang on cats!'  # Return the string 'Hello World!' as a response.


@app.route('/<greeting>/<person>')
def hello_person(greeting,person):  # try to name the function the same thing as the route before it
  return greeting + " " + person
app.run(debug=True)      # Run the app in debug mode.
        #name all of the files (server.py)

