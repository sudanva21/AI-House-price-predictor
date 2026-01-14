# 🏠 AI House Price Predictor

A Machine Learning-powered house price prediction application with support for **12 locations** across **India and USA**. Built with Python, Flask, and a beautiful Neumorphic UI.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![scikit-learn](https://img.shields.io/badge/sklearn-1.0+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📋 Table of Contents

- [Features](#-features)
- [Demo](#-demo)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Model Details](#-model-details)
- [Supported Locations](#-supported-locations)
- [API Reference](#-api-reference)
- [Technologies Used](#-technologies-used)
- [Future Improvements](#-future-improvements)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

- 🤖 **Machine Learning**: Linear Regression model trained on California Housing dataset
- 🌍 **Multi-Location Support**: 12 cities across India and USA
- 💱 **Smart Currency**: Automatic USD/INR display based on location
- 🎨 **Neumorphic UI**: Modern soft UI design with Outfit font
- 📊 **Real-time Predictions**: Instant price estimates via REST API
- 📱 **Responsive Design**: Works on desktop and mobile devices

---

## 🖥️ Demo

### Input Features
- Median Income (in $10,000)
- House Age (years)
- Average Rooms per household
- Average Bedrooms per household
- Block Population
- Average Occupancy
- Latitude & Longitude
- **Location Selection** (India/USA cities)

### Output
- Predicted house price in local currency (USD or INR)

---

## 🚀 Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/house-price-predictor.git
cd house-price-predictor
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install scikit-learn pandas joblib flask flask-cors numpy
```

### Step 3: Train the Model
```bash
python train_model.py
```

Expected output:
```
============================================================
HOUSE PRICE PREDICTION MODEL TRAINING
Enhanced with Location Features - India & USA
============================================================
Loading California Housing dataset...
Base dataset shape: (20640, 8)
Enhanced dataset shape: (247680, 10)
...
✅ TRAINING SUCCESSFULLY COMPLETED!
```

### Step 4: Start the Server
```bash
python app.py
```

### Step 5: Open the Application
Open `index.html` in your web browser.

---

## 📖 Usage

1. **Select a Location** from the dropdown (India or USA cities)
2. **Enter house features**:
   - Median Income
   - House Age
   - Average Rooms
   - Average Bedrooms
   - Population
   - Average Occupancy
   - Latitude & Longitude
3. **Click "Predict House Price"**
4. **View the result** in local currency (USD or INR)

---

## 📁 Project Structure

```
house-price-predictor/
│
├── 📄 train_model.py      # Model training script
├── 📄 app.py              # Flask API server
├── 📄 index.html          # Web interface (Neumorphic UI)
├── 📄 style.css           # CSS styling
├── 📄 script.js           # Frontend JavaScript
├── 📄 report.md           # Detailed project report
├── 📄 README.md           # This file
├── 📄 requirements.txt    # Python dependencies
│
└── 📁 models/             # Trained model artifacts
    ├── house_price_model.pkl
    ├── scaler.pkl
    ├── location_encoder.pkl
    ├── feature_columns.pkl
    └── locations.pkl
```

---

## 🧠 Model Details

| Attribute | Value |
|-----------|-------|
| Algorithm | Linear Regression |
| Base Dataset | California Housing (sklearn) |
| Training Samples | 198,144 |
| Test Samples | 49,536 |
| Features | 9 (8 housing + 1 location) |
| R² Score | ~0.58 |
| MSE | ~0.55 |

### Feature Importance
The model considers these features (ordered by importance):
1. Median Income (MedInc) - *Strongest predictor*
2. Location (encoded)
3. Average Rooms (AveRooms)
4. Latitude
5. Longitude
6. House Age
7. Population
8. Average Bedrooms
9. Average Occupancy

---

## 🌍 Supported Locations

### 🇺🇸 United States
| City | Price Multiplier |
|------|------------------|
| California | 1.00x (base) |
| New York | 1.35x |
| Washington | 1.15x |
| Florida | 0.90x |
| Texas | 0.75x |
| Illinois | 0.70x |

### 🇮🇳 India
| City | Price Multiplier | Currency |
|------|------------------|----------|
| Mumbai | 0.45x | ₹ INR |
| Bangalore | 0.40x | ₹ INR |
| Delhi | 0.35x | ₹ INR |
| Hyderabad | 0.30x | ₹ INR |
| Chennai | 0.28x | ₹ INR |
| Pune | 0.25x | ₹ INR |

**Currency Conversion**: 1 USD = ₹83.50 INR

---

## 📡 API Reference

### Health Check
```http
GET /health
```
**Response:**
```json
{
  "status": "ok",
  "model_loaded": true,
  "locations_available": ["California, USA", "Mumbai, India", ...]
}
```

### Get Locations
```http
GET /locations
```
**Response:**
```json
{
  "locations": ["California, USA", "New York, USA", "Mumbai, India", ...]
}
```

### Predict Price
```http
POST /predict
Content-Type: application/json
```
**Request Body:**
```json
{
  "Location": "Mumbai, India",
  "MedInc": 3.5,
  "HouseAge": 15,
  "AveRooms": 5.2,
  "AveBedrms": 1.0,
  "Population": 1200,
  "AveOccup": 3.0,
  "Latitude": 34.05,
  "Longitude": -118.24
}
```
**Response:**
```json
{
  "prediction": 1.8234,
  "price_usd": 182340.00,
  "location": "Mumbai, India",
  "unit": "hundred thousand USD"
}
```

---

## 🛠️ Technologies Used

| Category | Technology |
|----------|------------|
| **Backend** | Python, Flask, Flask-CORS |
| **ML/AI** | scikit-learn, pandas, numpy, joblib |
| **Frontend** | HTML5, CSS3, JavaScript |
| **UI Design** | Neumorphism (Soft UI) |
| **Typography** | Outfit (Google Fonts) |

---

## 🔮 Future Improvements

- [ ] Add more ML models (Random Forest, XGBoost, Neural Networks)
- [ ] Include more locations and countries
- [ ] Add real-time housing data integration
- [ ] Implement user authentication
- [ ] Deploy to cloud (Render, Vercel, AWS)
- [ ] Add price trend visualization charts
- [ ] Mobile app version (React Native)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)

---

## 🙏 Acknowledgments

- California Housing dataset from scikit-learn
- Neumorphic UI design inspiration
- Google Fonts (Outfit)

---

*Made with ❤️ for QSkill Internship - AI/ML Project*
