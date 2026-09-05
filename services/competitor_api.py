import pandas as pd

def create_competitor_csv():
    data = {
        "product_id": [101, 102, 103],
        "competitor_price": [480, 820, 310]
    }
    df = pd.DataFrame(data)
    df.to_csv("data/competitor_prices.csv", index=False)
    print("✅ competitor_prices.csv created!")

if __name__ == "__main__":
    create_competitor_csv()
