# Binance Futures Trading Bot (Testnet)

A simple Python-based **CLI trading bot** that places **Market and Limit orders** on the **Binance Futures Testnet (USDT‑M)**.  
This project demonstrates clean architecture, input validation, proper error handling, and file-based logging.

---

## 📌 Features

- Place **MARKET** and **LIMIT** orders  
- Supports both **BUY** and **SELL** sides  
- Uses **Binance Futures Testnet** (no real money involved)  
- Command Line Interface (CLI)  
- Input validation before order placement  
- Structured and reusable codebase  
- File-based logging for requests, responses, and errors  

---

## 🛠 Tech Stack

- Python 3.x  
- `python-binance`  
- `argparse`  
- Python built-in `logging`

---

## 📂 Project Structure

```
Binance-Trading-Bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py           # Binance Futures Testnet client
│   ├── orders.py           # Order placement logic
│   ├── validators.py       # Input validation
│   └── logging_config.py   # Logging configuration
│
├── logs/
│   └── trading_bot.log     # Generated log file
│
├── cli.py                  # CLI entry point
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone Binance-Trading-Bot
cd Binance-Trading-Bot
```

### 2️⃣ Create & Activate Virtual Environment

**Windows**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS**
```bash
python -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Environment Variables (Binance Futures Testnet)

**Windows (PowerShell)**
```powershell
$env:BINANCE_API_KEY="your_testnet_api_key"
$env:BINANCE_API_SECRET="your_testnet_api_secret"
```

**Linux / macOS**
```bash
export BINANCE_API_KEY="your_testnet_api_key"
export BINANCE_API_SECRET="your_testnet_api_secret"
```

> ⚠️ Use Binance Futures Testnet API keys only (not mainnet).

---

## ▶️ How to Run

### ✅ Place a MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### ✅ Place a LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 90000
```

---

## 📤 Sample Output

```
✅ Order placed successfully
Order ID     : 12107988978
Status       : NEW
Executed Qty : 0.000
Avg Price    : 0.00
```

> **Note:** On Binance Futures, MARKET orders may initially return `NEW` status. Execution happens immediately afterward and is normal behavior.

---

## 🧾 Logging

All logs are written to:
```
logs/trading_bot.log
```

Logs include:
- Order request summary
- Order response (orderId, status)
- Errors and failures

### Example Log Entry
```
2026-02-04 13:12:15 | INFO  | Placing MARKET order | BTCUSDT | BUY | qty=0.01
2026-02-04 13:12:16 | INFO  | MARKET order success | orderId=12107988978
```

---

## ❗ Assumptions

- User provides valid Binance Futures symbols
- API keys have Futures permissions enabled
- This project is strictly for testnet usage
- Input validation is handled before order placement

---

## 🚫 Out of Scope

- Real (mainnet) trading
- Spot trading
- Advanced order types (Stop‑Limit, OCO, TWAP, Grid)
- UI / Dashboard

---

## 🧠 Design Principles Used

- Separation of concerns
- Modular and reusable code
- Defensive programming
- Production-style logging

---

## 👤 Author

**SOAEB HASAN**  
Aspiring Python Developer
