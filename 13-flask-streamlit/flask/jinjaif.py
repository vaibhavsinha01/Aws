from flask import Flask, render_template, request

# {{ }} expression to print output in html
# {%...%} conditions,for loops
# {#...#} this is for comments

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to the Flask course</h1></html>"

@app.route("/index", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        # name = request.form.get('name')  # This also works
        name = request.form['name']
        return f"Hello {name}"
    return render_template("form.html")

@app.route('/successif/<int:score>')  # Variable rule
def successif(score):
    return render_template('result2.html',results=score)

if __name__ == "__main__":
    app.run(debug=True)
