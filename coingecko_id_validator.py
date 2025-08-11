
"""
LunorQuest Signal Boost CoinGecko ID Validator
----------------------
This script checks all unique `token_id` values from a given CSV file
against CoinGecko's API and prints whether they are valid.

Requirements:
    pip install pandas requests

Default CSV location: same folder as this script.
"""

import os
import pandas as pd
import requests

# === User Config ===
CSV_FILENAME = "signals.csv"  # Change to your CSV filename
COINGECKO_API = "https://api.coingecko.com/api/v3/coins/"
TIMEOUT = 10  # seconds

# === Load CSV ===
csv_path = os.path.join(os.path.dirname(__file__), CSV_FILENAME)
if not os.path.exists(csv_path):
    print(f"❌ CSV file not found: {csv_path}")
    exit(1)

try:
    df = pd.read_csv(csv_path)
except Exception as e:
    print(f"❌ Failed to read CSV: {e}")
    exit(1)

if "token_id" not in df.columns:
    print("❌ CSV missing required column: token_id")
    exit(1)

# Check if DataFrame has any data rows
if len(df) == 0:
    print("❌ CSV file has no data rows (only headers).")
    exit(1)

ids = sorted(set(df["token_id"].dropna().astype(str).str.strip()))
if not ids:
    print("❌ No valid token_id values found in CSV.")
    exit(1)

print("=== CoinGecko Token ID Validation ===")
for cid in ids:
    url = COINGECKO_API + cid
    try:
        r = requests.get(url, timeout=TIMEOUT)
        if r.status_code == 200:
            data = r.json()
            symbol = data.get("symbol", "?")
            name = data.get("name", "?")
            print(f"ID: {cid:<12} | Symbol: {symbol:<8} | Name: {name}")
        elif r.status_code == 404:
            print(f"ID: {cid:<12} | \033[91mNOT SUPPORTED\033[0m")
        else:
            print(f"ID: {cid:<12} | ❓ API Error ({r.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"ID: {cid:<12} | ⚠️ Request failed: {e}")
