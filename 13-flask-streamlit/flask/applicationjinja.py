from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to the Flask course</h1></html>"

@app.route('/successif/<int:score>')
def successif(score):
    return render_template('getresult.html', results=score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html', results=score)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        # Collect the form data
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c_programming = float(request.form['C'])
        datascience = float(request.form['datascience'])

        # Calculate total score
        total_score = (science + maths + c_programming + datascience) / 4

        # Redirect based on the score
        if total_score >= 50:
            return redirect(url_for('successif', score=total_score))
        else:
            return redirect(url_for('fail', score=total_score))
    return render_template('getresult.html')


if __name__ == "__main__":
    app.run(debug=True)
