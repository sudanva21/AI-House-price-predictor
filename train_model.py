"""
House Price Prediction Model - Enhanced Version
Includes location-based predictions for India and USA cities.
Uses California Housing dataset as base with location multipliers.
"""

import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import joblib
import os
import warnings

warnings.filterwarnings('ignore')

# Location price multipliers (relative to California base prices)
LOCATION_MULTIPLIERS = {
    # USA Cities
    'California, USA': 1.0,
    'New York, USA': 1.35,
    'Texas, USA': 0.75,
    'Florida, USA': 0.90,
    'Washington, USA': 1.15,
    'Illinois, USA': 0.70,
    # India Cities (converted to USD equivalent scale ~1/3rd)
    'Mumbai, India': 0.45,
    'Delhi, India': 0.35,
    'Bangalore, India': 0.40,
    'Hyderabad, India': 0.30,
    'Chennai, India': 0.28,
    'Pune, India': 0.25,
}

def create_enhanced_dataset():
    """Create enhanced dataset with location features."""
    print("Loading California Housing dataset...")
    california = fetch_california_housing()
    df_base = pd.DataFrame(california.data, columns=california.feature_names)
    df_base['BasePrice'] = california.target
    
    print(f"Base dataset shape: {df_base.shape}")
    print(f"Features: {list(california.feature_names)}")
    
    # Create expanded dataset with locations
    dfs = []
    for location, multiplier in LOCATION_MULTIPLIERS.items():
        df_loc = df_base.copy()
        df_loc['Location'] = location
        df_loc['Price'] = df_loc['BasePrice'] * multiplier
        dfs.append(df_loc)
    
    df = pd.concat(dfs, ignore_index=True)
    df = df.drop('BasePrice', axis=1)
    
    print(f"\nEnhanced dataset shape: {df.shape}")
    print(f"Total samples: {len(df):,}")
    print(f"Locations included: {len(LOCATION_MULTIPLIERS)}")
    for loc in LOCATION_MULTIPLIERS.keys():
        print(f"  • {loc}")
    
    return df, california.feature_names

def train_model():
    """Train the enhanced model with location features."""
    print("\n" + "="*60)
    print("HOUSE PRICE PREDICTION MODEL TRAINING")
    print("Enhanced with Location Features - India & USA")
    print("="*60)
    
    # 1. Create enhanced dataset
    df, base_features = create_enhanced_dataset()
    
    # 2. Encode location
    print("\nEncoding location features...")
    le = LabelEncoder()
    df['LocationEncoded'] = le.fit_transform(df['Location'])
    
    # Location mapping for reference
    print("\nLocation Encoding:")
    for loc in le.classes_:
        encoded = le.transform([loc])[0]
        print(f"  {encoded}: {loc}")
    
    # 3. Prepare features and target
    feature_cols = list(base_features) + ['LocationEncoded']
    X = df[feature_cols]
    y = df['Price']
    
    # 4. Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=df['LocationEncoded']
    )
    print(f"\nData Split:")
    print(f"  Training samples: {len(X_train):,}")
    print(f"  Test samples: {len(X_test):,}")
    
    # 5. Normalize features
    print("\nNormalizing features with StandardScaler...")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # 6. Train model
    print("\nTraining Linear Regression model...")
    model = LinearRegression()
    model.fit(X_train_scaled, y_train)
    print("Model training complete!")
    
    # 7. Evaluate
    y_pred = model.predict(X_test_scaled)
    
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print("\n" + "="*60)
    print("MODEL EVALUATION METRICS")
    print("="*60)
    print(f"  Mean Squared Error (MSE):      {mse:.4f}")
    print(f"  Root Mean Squared Error:       {rmse:.4f}")
    print(f"  Mean Absolute Error (MAE):     {mae:.4f}")
    print(f"  R-Squared Score (R²):          {r2:.4f}")
    print("="*60)
    
    # 8. Feature importance
    print("\nFEATURE IMPORTANCE (Absolute Coefficients):")
    print("-"*50)
    importance = pd.DataFrame({
        'Feature': feature_cols,
        'Coefficient': model.coef_
    })
    importance['AbsCoef'] = importance['Coefficient'].abs()
    importance = importance.sort_values('AbsCoef', ascending=False)
    
    for _, row in importance.iterrows():
        bar = "█" * int(row['AbsCoef'] * 10)
        print(f"  {row['Feature']:20s} {row['Coefficient']:+.4f} {bar}")
    
    # 9. Save artifacts
    print("\n" + "-"*50)
    print("SAVING MODEL ARTIFACTS")
    print("-"*50)
    os.makedirs('models', exist_ok=True)
    
    joblib.dump(model, 'models/house_price_model.pkl')
    joblib.dump(scaler, 'models/scaler.pkl')
    joblib.dump(le, 'models/location_encoder.pkl')
    joblib.dump(feature_cols, 'models/feature_columns.pkl')
    joblib.dump(list(LOCATION_MULTIPLIERS.keys()), 'models/locations.pkl')
    
    print("  ✓ house_price_model.pkl")
    print("  ✓ scaler.pkl")
    print("  ✓ location_encoder.pkl")
    print("  ✓ feature_columns.pkl")
    print("  ✓ locations.pkl")
    
    print("\n" + "="*60)
    print("✅ TRAINING SUCCESSFULLY COMPLETED!")
    print("="*60)
    
    return {
        'mse': mse,
        'rmse': rmse,
        'mae': mae,
        'r2': r2,
        'n_train': len(X_train),
        'n_test': len(X_test),
        'n_features': len(feature_cols),
        'n_locations': len(LOCATION_MULTIPLIERS),
        'locations': list(LOCATION_MULTIPLIERS.keys())
    }

if __name__ == "__main__":
    metrics = train_model()
