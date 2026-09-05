import pandas as pd

def create_features_csv():
    df = pd.read_csv("data/ecommerce_sales.csv")
    df['day_of_week'] = pd.to_datetime(df['timestamp']).dt.dayofweek
    df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
    df.to_csv("data/ecommerce_features.csv", index=False)
    print("✅ ecommerce_features.csv created!")

if __name__ == "__main__":
    create_features_csv()
