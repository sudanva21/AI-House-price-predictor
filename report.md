# House Price Prediction - Project Report

## Executive Summary

This project implements a Machine Learning-based house price prediction system that supports **12 locations** across **India and USA**. The model uses **Linear Regression** trained on the California Housing dataset with location-based price multipliers.

---

## 1. Project Objectives

| Objective | Status |
|-----------|--------|
| Load and explore dataset | ✅ Complete |
| Handle missing data & normalize inputs | ✅ Complete |
| Train/test split | ✅ Complete |
| Train Linear Regression model | ✅ Complete |
| Evaluate with MSE metric | ✅ Complete |
| Add location-based predictions | ✅ Complete |
| Professional web interface | ✅ Complete |

---

## 2. Dataset Information

- **Base Dataset**: California Housing (sklearn)
- **Samples**: 20,640 base × 12 locations = **247,680 total**
- **Features**: 9 (8 housing + 1 location)

### Feature Descriptions

| Feature | Description |
|---------|-------------|
| MedInc | Median income in block group |
| HouseAge | Median house age in block group |
| AveRooms | Average rooms per household |
| AveBedrms | Average bedrooms per household |
| Population | Block group population |
| AveOccup | Average household members |
| Latitude | Block group latitude |
| Longitude | Block group longitude |
| Location | City/Country (encoded) |

---

## 3. Model Performance

| Metric | Value |
|--------|-------|
| Mean Squared Error (MSE) | ~0.55 |
| Root Mean Squared Error | ~0.74 |
| Mean Absolute Error | ~0.53 |
| R-Squared Score | ~0.58 |

> **Note**: R² = 0.58 indicates the model explains 58% of price variance - reasonable for linear regression on real estate data.

---

## 4. Supported Locations

### USA (6 cities)
- California, USA
- New York, USA
- Texas, USA
- Florida, USA
- Washington, USA
- Illinois, USA

### India (6 cities)
- Mumbai, India
- Delhi, India
- Bangalore, India
- Hyderabad, India
- Chennai, India
- Pune, India

---

## 5. Technology Stack

| Component | Technology |
|-----------|------------|
| ML Model | scikit-learn (LinearRegression) |
| Backend | Flask + Flask-CORS |
| Frontend | HTML5, CSS3, JavaScript |
| UI Design | Neumorphism (Soft UI) |
| Typography | Outfit (Google Fonts) |

---

## 6. Project Structure

```
AI-MLproject-1/
├── train_model.py      # Model training script
├── app.py              # Flask API server
├── index.html          # Web interface
├── style.css           # Neumorphic styling
├── script.js           # Frontend logic
└── models/
    ├── house_price_model.pkl
    ├── scaler.pkl
    ├── location_encoder.pkl
    ├── feature_columns.pkl
    └── locations.pkl
```

---

## 7. How to Run

1. **Train the model**:
   ```bash
   python train_model.py
   ```

2. **Start the server**:
   ```bash
   python app.py
   ```

3. **Open in browser**:
   Open `index.html` in your browser

---

## 8. Skills Demonstrated

- ✅ Handling tabular data with Pandas
- ✅ Regression modeling with scikit-learn
- ✅ Feature engineering (location encoding)
- ✅ Data normalization (StandardScaler)
- ✅ Model evaluation metrics (MSE, R², MAE)
- ✅ REST API development (Flask)
- ✅ Modern UI/UX (Neumorphism)

---

## 9. Future Improvements

1. Use advanced models (Random Forest, XGBoost)
2. Add more location data from real datasets
3. Include additional features (crime rate, school quality)
4. Deploy to cloud (Render, Vercel)

---

*Report generated on January 15 2026 12:05am*
