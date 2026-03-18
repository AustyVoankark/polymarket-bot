# Polymarket BTC Trading Bot

Automated trading bot for BTC price prediction markets on Polymarket using technical analysis.

## Strategy

The bot monitors 5-minute candlestick data on BTC price prediction markets and executes trades when:

1. **Green candle detected** - Close price > Open price
2. **High volume confirmed** - Current volume > 20-period average volume

Only trades active markets with sufficient liquidity (configurable threshold).

## Requirements

- Python 3.10+
- Polymarket account with API access
- USDC balance on Polygon network

## Installation

### 1. Clone or download this directory

```bash
cd polymarket-bot
```

### 2. Create a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Get Polymarket API Credentials

1. Go to https://polymarket.com/portfolio/api-keys
2. Generate a new API key pair
3. Copy your API Key and API Secret

### 5. Configure credentials

```bash
# Copy the example file
cp .env.example .env

# Edit .env with your credentials
# Windows
notepad .env

# macOS/Linux
nano .env
```

Add your API credentials:

```
POLYMARKET_API_KEY=your_actual_api_key
POLYMARKET_API_SECRET=your_actual_api_secret
```

**⚠️ SECURITY WARNING:**
- Never commit `.env` to version control
- Never share your API secret
- Keep your credentials private

## Running the Bot

### Start the bot

```bash
python bot.py
```

The bot will:
1. Connect to Polymarket API
2. Scan for active BTC markets
3. Analyze each market for trading signals
4. Execute trades when conditions are met
5. Log all activity to `trading_log.txt`

### Stop the bot

Press `Ctrl+C` to stop the bot gracefully.

## Configuration

Edit `.env` to customize settings:

| Setting | Default | Description |
|---------|---------|-------------|
| `TRADE_SIZE_USDC` | 10.0 | Size of each trade in USDC |
| `MIN_MARKET_LIQUIDITY` | 1000.0 | Minimum market liquidity required |
| `VOLUME_THRESHOLD_MULTIPLIER` | 1.0 | Volume must exceed avg × this value |
| `VOLUME_AVERAGE_PERIODS` | 20 | Number of candles for volume average |
| `MARKET_REFRESH_INTERVAL` | 60 | Seconds between market scans |
| `CANDLE_TIMEFRAME_MINUTES` | 5 | Candlestick timeframe |

## Reading the Logs

All activity is logged to `trading_log.txt`:

### Log Format

```
2026-03-16 23:45:00 | INFO     | ACTION: Scanning for BTC markets
2026-03-16 23:45:01 | INFO     | MARKET SCAN | Found: 5 | Eligible: 3
2026-03-16 23:45:02 | INFO     | SIGNAL: GREEN_CANDLE_HIGH_VOLUME | Market: 0x123...
2026-03-16 23:45:03 | INFO     | TRADE EXECUTED
```

### Trade Execution Log

When a trade is executed, you'll see:

```
================================================================================
TRADE EXECUTED
================================================================================
Timestamp: 2026-03-16T23:45:03.123456
Market ID: 0x123abc...
Market: Will BTC be above $65,000 on March 17?
Side: YES
Price: 0.6500
Size: 10.00 USDC
Outcome: BUY
Order ID: order_12345
================================================================================
```

### Error Logs

Errors include full tracebacks at DEBUG level:

```
2026-03-16 23:45:00 | ERROR    | ERROR: PolymarketAPIError: Request failed
2026-03-16 23:45:00 | DEBUG    | TRACEBACK:
Traceback (most recent call last):
  ...
```

## Project Structure

```
polymarket-bot/
├── bot.py           # Main bot logic and trading loop
├── config.py        # Configuration settings
├── logger.py        # Logging utilities
├── requirements.txt # Python dependencies
├── .env.example     # Example environment file
├── .env             # Your actual credentials (create from .env.example)
├── README.md        # This file
└── trading_log.txt  # Generated log file
```

## Risk Warning

**Trading involves significant risk. This bot is for educational purposes.**

- Only trade with funds you can afford to lose
- Test thoroughly with small amounts first
- Monitor the bot regularly
- Prediction markets can be highly volatile
- Past performance does not guarantee future results

## Troubleshooting

### "Missing Polymarket API credentials"

Ensure your `.env` file exists and contains valid `POLYMARKET_API_KEY` and `POLYMARKET_API_SECRET`.

### "Insufficient balance"

Your USDC balance is below `TRADE_SIZE_USDC`. Add USDC to your Polymarket wallet.

### "No eligible markets found"

No BTC markets meet the liquidity threshold. Try lowering `MIN_MARKET_LIQUIDITY`.

### Rate limiting errors

The bot has built-in retry logic. If issues persist, increase `MARKET_REFRESH_INTERVAL`.

## License

MIT License - Use at your own risk.

## Support

For Polymarket API issues: https://docs.polymarket.com
