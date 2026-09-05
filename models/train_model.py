import pandas as pd
import xgboost as xgb
import joblib

def train_and_save_model():
    # Load engineered features
    df = pd.read_csv("data/ecommerce_features.csv")

    # Choose target column
    target_col = "optimal_price"   # <-- we want to predict this
    y = df[target_col]
    X = df.drop(columns=[target_col])

    # --- Fix problematic dtypes ---
    if "timestamp" in X.columns:
        X["timestamp"] = pd.to_datetime(X["timestamp"], errors="coerce")
        X["timestamp"] = X["timestamp"].astype("int64") // 10**9

    if "season" in X.columns:
        X["season"] = X["season"].astype("category").cat.codes

    print("Feature dtypes:\n", X.dtypes)

    # Train XGBoost model
    model = xgb.XGBRegressor(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=5,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42,
        enable_categorical=True
    )

    model.fit(X, y)

    # Save model
    joblib.dump(model, "models/model.pkl")
    print("✅ Model trained and saved to models/model.pkl")

if __name__ == "__main__":
    train_and_save_model()
