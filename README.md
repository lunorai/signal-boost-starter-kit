# 🧠 SignalBoost Quest by Lunor

Welcome to the official repository for the **SignalBoost Quest**, powered by **Lunor**.

---

## 📚 Table of Contents

1. [📜 Description](#-description)
2. [🎯 Objective](#-objective)
3. [🗂️ Submission Format (CSV)](#-submission-format-csv)
4. [🏷️ Supported Labels](#-supported-labels)
5. [⚖️ Validation & Rejection Rules](#-validation--rejection-rules)
6. [🔍 Submission Validation & Rewards Guide](#-submission-validation--rewards-guide)
   - [🔍 Submission Validation](#-submission-validation)
   - [💰 Reward Distribution](#-reward-distribution)
   - [🏆 Private Leaderboard Eligibility](#-private-leaderboard-eligibility)
   - [✅ Submission Checklist](#-submission-checklist)
7. [🚀 Local Submission Validation & CoinGecko ID Check](#-local-submission-validation--coingecko-id-check)
   - [🔧 How to Run Pre-Check Script](#-how-to-run-pre-check-script)
   - [🔧 How to Run CoinGecko ID Validator](#-how-to-run-coingecko-id-validator)
8. [💬 Support & Community](#-support--community)

---

## 📜 Description

Crypto markets move at lightning speed — and often, it’s the right news at the right time that drives massive token-specific moves.

But not all news is equal.

This Lunor Quest challenges you to curate **real, verifiable news events** — tweets, articles, announcements — that had an immediate and measurable impact on a specific token’s price.  
Think **listings, hacks, funding rounds, or governance changes** that actually moved the market.

Your goal is to help build a **high-signal training dataset** for AI systems that can:

- Detect breaking news faster
- Predict market impact with precision
- Separate signal from noise in the chaotic world of crypto

Submissions must be **timestamped** and tagged with the correct event type and token using its **Coingecko ID**.  
Backend validation will verify listing status, market cap, volatility, and price movement using live on-chain data and exchange feeds via **CCXT**.

**Better news curation = higher Signal Score = bigger rewards.**

---

## 🎯 Objective

Submit timestamped news events that:

- Are directly tied to a specific token
- Happened **after** the token was listed on a top-tier exchange
- Triggered noticeable token-specific price movement
- Are tagged with the correct label type
- Include the Coingecko token ID for automated validation

---

## 🗂️ Submission Format (CSV)

**Format:**

```csv
title,type,timestamp_utc,source,label,token_id
```

---

## 🏷️ Supported Labels

This document outlines the list of supported labels categorized for easier reference.

## 📈 Market & Trading

- `listing`
- `delisting`
- `trading_pair_change`

## 🔐 Security & Risk

- `hack`
- `rugpull`
- `security_breach`
- `downtime`

## 🏛️ Protocol & Governance

- `mainnet_launch`
- `upgrade`
- `governance_proposal`
- `rebrand`

## 💰 Token Economics

- `token_burn`
- `token_unlock`
- `airdrop`
- `staking_update`
- `supply_inflation`

## 🌐 Ecosystem & Partnerships

- `partnership`
- `product_launch`
- `infrastructure_integration`
- `chain_migration`

## 💵 Fundraising & Treasury

- `funding_round`
- `grant_award`
- `treasury_update`

## 👥 Team & Legal

- `team_change`
- `legal_action`
- `regulatory_news`

## 🌍 Macro & Industry

- `macro_event`
- `industry_merger`
- `infrastructure_outage`

## 🎭 Community & Culture

- `community_conflict`
- `social_trend`
- `celebrity_endorsement`

````


## ⚖️ Validation & Rejection Rules

### ✅ Accepted If:

- News occurred **after** the token was listed
- Price movement is **significant** and token-specific
- **Coingecko ID** is valid and retrievable via API
- Token’s **market cap** at the time of the event is **> $30M**
- Token is **not a stablecoin**

### ❌ Rejected If:

- **Duplicate source** (only first valid submission is accepted)
- News timestamp is within **2 hours before** listing on exchange
- Token **not listed** at timestamp of event
- Token market cap **≤ $30M**
- Token is a **stablecoin**
- Price movement **< 1.0%** (Signal Score < 1 earns no points)

---

# 🔍 Submission Validation & Rewards Guide

## 🔍 Submission Validation

### 🔗 Token Resolution via Coingecko

1. Retrieve token markets from **Coingecko**.
2. Filter out:
   - Unstable pairs
   - Inactive pairs
   - Unsupported pairs
3. Rank by **trust score** & **volume**.
4. Choose the top **CCXT-compatible** pair for price analysis.

### 📊 Price Data from CCXT

- Fetch **minute-level OHLCV** starting **5 minutes after news**.
- Analyze price change over:
  - 15 minutes
  - 1 hour
  - 4 hours
  - 12 hours
- Compare with **BTC** price movement to calculate **relative impact**.

---

## 💰 Reward Distribution

Rewards are **linear** based on the total **Signal Score** from valid submissions.
**Max counted score per participant** = `10,000`

**Formula:**

```math
Your Reward = (Your Score ÷ Sum of All Scores) × Total Prize Pool
````

**Minimum eligibility:** 100 total Signal Score

---

### 🏆 Private Leaderboard Eligibility

To appear on the private leaderboard & receive rewards:

- **Achieve** ≥ 100 total Signal Score
- **Submit** at least **10–15 high-quality**, scored news items

---

### ✅ Submission Checklist

- Token is **listed before event timestamp**
- **No duplicate** source URL
- Not within **2h before listing** (for listing news)
- Not a **stablecoin**
- **Market cap** > $30M

---

## 🚀 Local Submission Validation & CoinGecko ID Check

Before submitting your signals, you can validate your CSV locally and check your CoinGecko token IDs.

### 🔧 How to Run Pre-Check Script

This script checks your CSV for formatting, required columns, allowed labels, and timestamp formats.

**Requirements:**

- Python 3.x
- pandas

**Install dependencies:**

```sh
pip install pandas
```

**Run the pre-check script:**

```sh
python pre-check-submission.py
```

- By default, it checks `signals.csv` in the same folder.
- Fix any errors shown before submitting.

### 🔧 How to Run CoinGecko ID Validator

This script verifies that all `token_id` values in your CSV are valid CoinGecko IDs.

**Requirements:**

- Python 3.x
- pandas
- requests

**Install dependencies:**

```sh
pip install pandas requests
```

**Run the validator:**

```sh
python coingecko_id_validator.py
```

- By default, it checks `signals.csv` in the same folder.
- Review the output to ensure all IDs are supported.

---

### 💬 Support & Community

Join our Discord for updates, strategy discussions, and help:  
👉 [discord.gg/6NrZmpPpTY](https://discord.gg/6NrZmpPpTY)

---

<p align="center">
  <img src="/signal-boost-starter-kit/lunor-full.png" alt="Lunor" width="120"/>
  <br>
  <b>SignalBoost Quest is brought to you by Lunor</b>
</p>
