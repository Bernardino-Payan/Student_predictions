import os
from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

# Load the trained model and encoder
model = joblib.load("student.pkl")
encoder = joblib.load("student_encoder.pkl")

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form data
        math_score = float(request.form["math_score"])
        reading_score = float(request.form["reading_score"])
        writing_score = float(request.form["writing_score"])

        # Prepare input data
        input_features = np.array([[math_score, reading_score, writing_score]])

        # Make prediction
        prediction = model.predict(input_features)
        predicted_class = encoder.inverse_transform(prediction)[0]

        return jsonify({"prediction": predicted_class})

    except Exception as e:
        return jsonify({"error": str(e)})

# Run the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Heroku's assigned port
    app.run(host="0.0.0.0", port=port)
