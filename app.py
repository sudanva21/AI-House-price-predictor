"""
Flask Backend for House Price Prediction
Supports location-based predictions for India and USA cities.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import os

app = Flask(__name__)
CORS(app)

# Load model artifacts
MODEL_PATH = 'models/house_price_model.pkl'
SCALER_PATH = 'models/scaler.pkl'
ENCODER_PATH = 'models/location_encoder.pkl'
FEATURES_PATH = 'models/feature_columns.pkl'
LOCATIONS_PATH = 'models/locations.pkl'

model = None
scaler = None
location_encoder = None
feature_cols = None
locations = None

def load_artifacts():
    global model, scaler, location_encoder, feature_cols, locations
    try:
        model = joblib.load(MODEL_PATH)
        scaler = joblib.load(SCALER_PATH)
        location_encoder = joblib.load(ENCODER_PATH)
        feature_cols = joblib.load(FEATURES_PATH)
        locations = joblib.load(LOCATIONS_PATH)
        print("✓ All model artifacts loaded successfully!")
        print(f"  Supported locations: {locations}")
        return True
    except Exception as e:
        print(f"✗ Error loading artifacts: {e}")
        return False

# Load on startup
artifacts_loaded = load_artifacts()

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "status": "House Price Prediction API is running",
        "endpoints": {
            "/predict": "POST - Get price prediction",
            "/locations": "GET - List supported locations",
            "/health": "GET - Server health check"
        }
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "ok",
        "model_loaded": model is not None,
        "locations_available": locations if locations else []
    })

@app.route('/locations', methods=['GET'])
def get_locations():
    """Return list of supported locations."""
    if locations:
        return jsonify({"locations": locations})
    return jsonify({"error": "Locations not loaded"}), 500

@app.route('/predict', methods=['POST'])
def predict():
    if model is None or scaler is None:
        return jsonify({"error": "Model not loaded. Run train_model.py first."}), 500
    
    try:
        data = request.json
        
        # Get location and encode it
        location = data.get('Location')
        if location not in locations:
            return jsonify({
                "error": f"Invalid location. Supported: {locations}"
            }), 400
        
        location_encoded = location_encoder.transform([location])[0]
        
        # Features in order: MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude, LocationEncoded
        features = [
            float(data.get('MedInc', 0)),
            float(data.get('HouseAge', 0)),
            float(data.get('AveRooms', 0)),
            float(data.get('AveBedrms', 0)),
            float(data.get('Population', 0)),
            float(data.get('AveOccup', 0)),
            float(data.get('Latitude', 0)),
            float(data.get('Longitude', 0)),
            float(location_encoded)
        ]
        
        # Scale and predict
        features_scaled = scaler.transform([features])
        prediction = model.predict(features_scaled)[0]
        
        # Convert to actual price (multiply by 100,000 for display)
        price_usd = prediction * 100000
        
        return jsonify({
            "prediction": round(prediction, 4),
            "price_usd": round(price_usd, 2),
            "location": location,
            "unit": "hundred thousand USD"
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    print("\n" + "="*50)
    print("HOUSE PRICE PREDICTION SERVER")
    print("="*50)
    # Use PORT environment variable for Render, default to 5000 for local
    port = int(os.environ.get('PORT', 5000))
    # host='0.0.0.0' is required for Render to be accessible externally
    app.run(host='0.0.0.0', port=port)
