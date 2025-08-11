#!/usr/bin/env python3
"""
LunorQuest Signal Boost CSV Pre-Check Script
------------------------------------
This script validates your CSV submissions BEFORE you send them.
It ensures:
    1. Correct column names
    2. No empty cells
    3. Each row has exactly the expected number of columns
    4. Only ONE label per row (no commas)
    5. Label is in the allowed list (see list below)
    6. Timestamps are in correct UTC format (YYYY-MM-DDTHH:MM:SSZ)

------------------------------------
INSTALLATION:
    You need Python 3.x and pandas.

    Install required libraries by running:
        pip install pandas

------------------------------------
CSV LOCATION:
    By default, the script looks for the file in the same folder as this script.
    Change the `CSV_FILE` variable below if your file is elsewhere.

------------------------------------
CSV FORMAT:
    Required columns (in any order):
        title, type, timestamp_utc, token_id, source, label

    Timestamp format: 2024-01-15T10:30:00Z (ISO 8601 with Z suffix)
    Token ID format: Use CoinGecko token ID (e.g., "bitcoin", "ethereum", "pepe")
    Source format: Must be a valid HTTP/HTTPS URL

------------------------------------
ALLOWED LABELS:
    # Market & Trading
    listing, delisting, trading_pair_change

    # Security & Risk
    hack, rugpull, security_breach, downtime

    # Protocol & Governance
    mainnet_launch, upgrade, governance_proposal, rebrand

    # Token Economics
    token_burn, token_unlock, airdrop, staking_update, supply_inflation

    # Ecosystem & Partnerships
    partnership, product_launch, infrastructure_integration, chain_migration

    # Fundraising & Treasury
    funding_round, grant_award, treasury_update

    # Team & Legal
    team_change, legal_action, regulatory_news

    # Macro & Industry
    macro_event, industry_merger, infrastructure_outage

    # Community & Culture
    community_conflict, social_trend, celebrity_endorsement
"""

import os
import pandas as pd
from datetime import datetime

# ------------------------------------
# USER CONFIGURATION
# ------------------------------------
# Default: looks for file in same folder as script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(SCRIPT_DIR, "signals.csv")  # Change if needed

# Hardcoded allowed labels
ALLOWED_LABELS = [
    "listing", "delisting", "trading_pair_change",
    "hack", "rugpull", "security_breach", "downtime",
    "mainnet_launch", "upgrade", "governance_proposal", "rebrand",
    "token_burn", "token_unlock", "airdrop", "staking_update", "supply_inflation",
    "partnership", "product_launch", "infrastructure_integration", "chain_migration",
    "funding_round", "grant_award", "treasury_update",
    "team_change", "legal_action", "regulatory_news",
    "macro_event", "industry_merger", "infrastructure_outage",
    "community_conflict", "social_trend", "celebrity_endorsement"
]

EXPECTED_COLUMNS = [
    "title", "type", "timestamp_utc", "token_id", "source", "label"
]

# ------------------------------------
# VALIDATION LOGIC
# ------------------------------------
def validate_csv(file_path):
    errors = []
    
    try:
        df = pd.read_csv(file_path, dtype=str)
    except Exception as e:
        return [f"❌ Failed to read CSV: {e}"]

    # 1. Check if CSV has data rows
    if len(df) == 0:
        errors.append("❌ CSV file has no data rows (only headers). Please add your signal data.")

    # 2. Check columns (order doesn't matter)
    expected_set = set(EXPECTED_COLUMNS)
    found_set = set(df.columns)
    
    if expected_set != found_set:
        missing = expected_set - found_set
        extra = found_set - expected_set
        errors.append(f"❌ Column names mismatch.")
        errors.append(f"   Expected: {EXPECTED_COLUMNS}")
        errors.append(f"   Found:    {list(df.columns)}")
        if missing:
            errors.append(f"   Missing:  {list(missing)}")
        if extra:
            errors.append(f"   Extra:    {list(extra)}")

    # 3. Check for empty cells
    if df.isnull().values.any() or (df == "").values.any():
        errors.append("❌ Found empty cells — all fields must be populated.")

    # 4. Check column count per row
    with open(file_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            if len(line.strip().split(",")) != len(EXPECTED_COLUMNS):
                errors.append(f"❌ Row {i} does not have exactly {len(EXPECTED_COLUMNS)} columns.")

    # 5. Check single label only (no commas)
    for idx, label in enumerate(df["label"], start=2):  # header = row 1
        if "," in label:
            errors.append(f"❌ Row {idx} has multiple labels: '{label}'")

    # 6. Check label is in allowed list
    for idx, label in enumerate(df["label"], start=2):
        if label not in ALLOWED_LABELS:
            errors.append(f"❌ Row {idx} has invalid label: '{label}'")

    # 7. Check timestamp format
    for idx, ts in enumerate(df["timestamp_utc"], start=2):
        try:
            # Check for ISO format with T and Z (e.g., "2024-01-15T10:30:00Z")
            datetime.fromisoformat(ts.replace('Z', '+00:00'))
        except ValueError:
            errors.append(f"❌ Row {idx} has invalid timestamp format: '{ts}' (expected YYYY-MM-DDTHH:MM:SSZ)")

    return errors

# ------------------------------------
# MAIN EXECUTION
# ------------------------------------
if __name__ == "__main__":
    print(f"🔍 Validating file: {CSV_FILE}")
    results = validate_csv(CSV_FILE)

    if results:
        print("\n".join(results))
        print("❌ Validation failed. Please fix the above issues.")
    else:
        print("✅ CSV passed all validation checks! Ready for submission.")
