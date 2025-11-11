import requests
import pandas as pd
import os
import datetime
from dotenv import load_dotenv
import json

# Load biến môi trường từ file .env
load_dotenv()
METALPRICE_API_KEY = os.getenv("METALPRICE_API_KEY")  # ✅ Lấy key từ biến môi trường

def extract_gold_data(output_path="data/raw/metalprice_gold.json"):
    """
    Extract step:
    - Gọi MetalpriceAPI để lấy giá vàng (XAU) và tỷ giá USD/VND
    - Lưu dữ liệu raw vào local
    - Tính giá vàng theo USD và VND
    """
    url = f"https://api.metalpriceapi.com/v1/latest?api_key={METALPRICE_API_KEY}&base=USD&currencies=XAU,VND"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"❌ Extract error: {response.status_code} - {response.text}")

    data = response.json()
    timestamp = datetime.datetime.fromtimestamp(data["timestamp"])

    # Lưu bản raw JSON
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"[✅] Raw data saved to {output_path}")

    # Tính giá vàng theo ounce
    rates = data["rates"]
    price_usd_per_ounce = 1 / rates["XAU"]
    vnd_per_usd = rates["VND"]
    price_vnd_per_ounce = price_usd_per_ounce * vnd_per_usd

    df = pd.DataFrame([{
        "timestamp": timestamp,
        "price_usd_per_ounce": round(price_usd_per_ounce, 2),
        "price_vnd_per_ounce": round(price_vnd_per_ounce, 0)
    }])

    print(df)
    return df


def save_to_csv(df, path="data/raw/gold_price.csv"):
    """Lưu dữ liệu vào file CSV"""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    print(f"[✅] Clean data saved to {path}")


if __name__ == "__main__":
    df = extract_gold_data()
    save_to_csv(df)