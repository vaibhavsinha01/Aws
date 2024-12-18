from flask import Flask

app = Flask(__name__) # creates an instance of class which will be the WSGI(web server gateway interface) application.

# for creation of homepage
@app.route("/") # this is the route 
def welcome():
    return "Welcome to this Flask course. This should be an amazing course" # message displayed on the site

@app.route("/index")
def index():
    return "Welcome to the index page."

if __name__ == "__main__":
    app.run(debug=True) # changes are made dynamically no need to re-run the program
