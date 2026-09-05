import pandas as pd

def create_sales_csv():
    data = {
        "timestamp": ["2026-09-01 10:00:00", "2026-09-01 11:00:00", "2026-09-01 12:00:00"],
        "product_id": [101, 102, 103],
        "demand": [20, 35, 15],
        "inventory": [100, 50, 200],
        "season": ["festive", "regular", "regular"],
        "optimal_price": [499, 799, 299]
    }
    df = pd.DataFrame(data)
    df.to_csv("data/ecommerce_sales.csv", index=False)
    print("✅ ecommerce_sales.csv created!")

if __name__ == "__main__":
    create_sales_csv()
