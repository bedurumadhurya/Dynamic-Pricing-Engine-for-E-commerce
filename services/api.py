from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="Dynamic Pricing API")

# Load trained model safely
try:
    model = joblib.load("models/model.pkl")
except Exception as e:
    model = None
    print("⚠️ Error loading model:", e)

# Define input schema
class PriceRequest(BaseModel):
    timestamp: str
    product_id: int
    demand: float
    inventory: float
    season: str
    day_of_week: int
    hour: int

# ✅ Custom HTML landing page
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Dynamic Pricing API</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
                h1 { color: #2E86C1; }
                p { font-size: 18px; }
                a { text-decoration: none; color: #27AE60; font-weight: bold; }
            </style>
        </head>
        <body>
            <h1>🚀 Dynamic Pricing API</h1>
            <p>Your backend is live and ready to predict prices!</p>
            <p>Use <a href="/docs">Swagger Docs</a> to test endpoints.</p>
        </body>
    </html>
    """

@app.post("/predict")
def predict_price(request: PriceRequest):
    if model is None:
        return {"error": "Model not loaded. Check path to model.pkl"}

    try:
        data = pd.DataFrame([{
            "timestamp": int(pd.to_datetime(request.timestamp).timestamp()),
            "product_id": request.product_id,
            "demand": request.demand,
            "inventory": request.inventory,
            "season": pd.Categorical([request.season]).codes[0],
            "day_of_week": request.day_of_week,
            "hour": request.hour
        }])
        prediction = model.predict(data)[0]
        return {"predicted_optimal_price": round(float(prediction), 2)}
    except Exception as e:
        return {"error": str(e)}
