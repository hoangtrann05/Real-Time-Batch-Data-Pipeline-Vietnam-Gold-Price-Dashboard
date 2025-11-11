


import requests
import pandas as pd
import datetime
import os
import json
from dotenv import load_dotenv

# Load API key từ .env
load_dotenv()
API_KEY = os.getenv("METALPRICE_API_KEY")

def extract_gold_data_range(days=7, save_path="data/raw/gold_history.csv"):
    """
    Lấy dữ liệu giá vàng trong nhiều ngày (historical load)
    - days: số ngày muốn lấy (tính từ hôm nay)
    - save_path: đường dẫn lưu file CSV kết quả
    """
    base_url = "https://api.metalpriceapi.com/v1"
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=days)

    results = []

    for i in range(days):
        date = (start_date + datetime.timedelta(days=i)).strftime("%Y-%m-%d")
        url = f"{base_url}/{date}?api_key={API_KEY}&base=USD&currencies=XAU,VND"
        print(f"[⏳] Fetching data for {date} ...")

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            rates = data.get("rates", {})
            if "XAU" in rates and "VND" in rates:
                price_usd = 1 / rates["XAU"]
                price_vnd = price_usd * rates["VND"]
                results.append({
                    "date": date,
                    "price_usd_per_ounce": round(price_usd, 2),
                    "price_vnd_per_ounce": round(price_vnd, 0)
                })
            else:
                print(f"[⚠️] Missing rate data for {date}")
        else:
            print(f"[❌] Failed {date}: {response.status_code}")

    # Lưu kết quả ra file CSV
    df = pd.DataFrame(results)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df.to_csv(save_path, index=False)
    print(f"[✅] Saved {len(df)} records to {save_path}")
    return df


if __name__ == "__main__":
    df = extract_gold_data_range(days=30)
    print(df.tail())