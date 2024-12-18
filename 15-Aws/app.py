from flask import Flask, request, render_template
import pickle
import numpy as np

# Initialize the Flask application
application = Flask(__name__)
app = application

# Load the trained model
model = pickle.load(open("regressor.pkl", "rb"))

@app.route("/")
def index():
    # Render the main page
    return render_template('home.html')

@app.route("/predictdata", methods=['POST'])
def predict_datapoint():
    if request.method == "POST":
        try:
            # Collect form data
            Temperature = float(request.form['Temperature'])
            RH = float(request.form['RH'])
            Ws = float(request.form['Ws'])
            Rain = float(request.form['Rain'])
            FFMC = float(request.form['FFMC'])
            DMC = float(request.form['DMC'])
            DC = float(request.form['DC'])
            ISI = float(request.form['ISI'])
            BUI = float(request.form['BUI'])
            FWI = float(request.form['FWI'])
            Region = int(request.form['Region'])

            # Prepare data for prediction
            input_data = np.array([[Temperature, RH, Ws, Rain, FFMC, DMC, DC, ISI, BUI, FWI, Region]])
            
            # Make prediction
            prediction = model.predict(input_data)
            
            # Return the result to the template
            return render_template('home.html', prediction_text=f"Predicted Value: {prediction[0]:.2f}")
        except Exception as e:
            return render_template('home.html', prediction_text=f"Error: {e}")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
