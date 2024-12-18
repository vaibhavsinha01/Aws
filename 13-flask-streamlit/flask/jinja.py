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

@app.route('/successres/<int:score>')  # Variable rule
def successres(score):
    # Determine the result based on the score
    if score > 50:
        res = "Pass"
    else:
        res = "Fail"

    exp = {'score':score,'res':res}
    # Ensure return statement is outside the if-else block
    # return render_template('result.html', result=res)
    return render_template('result1.html',result=exp)

if __name__ == "__main__":
    app.run(debug=True)
