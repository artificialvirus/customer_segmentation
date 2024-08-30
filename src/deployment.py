# deployment.py

from flask import Flask, request, jsonify
import joblib
import pandas as pd
import logging

app = Flask(__name__)

# Load model
model = joblib.load('../models/kmeans_model.pkl')

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        df = pd.DataFrame(data)
        
        # Input validation (basic example)
        required_columns = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)', 'Gender_Female', 'Gender_Male']
        if not all(column in df.columns for column in required_columns):
            return jsonify({"error": "Missing required columns"}), 400

        predictions = model.predict(df)
        
        # Log the request and the response
        logging.info(f"Received data: {df.to_dict(orient='records')}")
        logging.info(f"Predictions: {predictions.tolist()}")
        
        return jsonify(predictions.tolist())
    
    except Exception as e:
        logging.error(f"Error during prediction: {str(e)}")
        return jsonify({"error": "An error occurred during prediction"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
