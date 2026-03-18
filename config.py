"""
Configuration settings for Polymarket trading bot.

All sensitive credentials are loaded from environment variables.
Copy .env.example to .env and fill in your values.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# =============================================================================
# API Credentials (loaded from environment variables)
# =============================================================================

POLYMARKET_API_KEY = os.getenv("POLYMARKET_API_KEY")
POLYMARKET_API_SECRET = os.getenv("POLYMARKET_API_SECRET")
POLYMARKET_CHAIN_ID = int(os.getenv("POLYMARKET_CHAIN_ID", "137"))  # Polygon mainnet

# Validate credentials are present
if not POLYMARKET_API_KEY or not POLYMARKET_API_SECRET:
    raise ValueError(
        "Missing Polymarket API credentials. "
        "Set POLYMARKET_API_KEY and POLYMARKET_API_SECRET in your .env file."
    )


# =============================================================================
# Trading Settings
# =============================================================================

# Size of each trade in USDC
TRADE_SIZE_USDC = float(os.getenv("TRADE_SIZE_USDC", "10.0"))

# Minimum liquidity required in a market to trade (USDC)
MIN_MARKET_LIQUIDITY = float(os.getenv("MIN_MARKET_LIQUIDITY", "1000.0"))

# Volume threshold multiplier (trade when volume > avg_volume * this value)
VOLUME_THRESHOLD_MULTIPLIER = float(os.getenv("VOLUME_THRESHOLD_MULTIPLIER", "1.0"))

# Number of periods for average volume calculation
VOLUME_AVERAGE_PERIODS = int(os.getenv("VOLUME_AVERAGE_PERIODS", "20"))


# =============================================================================
# Market Settings
# =============================================================================

# Keywords to search for BTC price prediction markets
BTC_MARKET_KEYWORDS = [
    "BTC",
    "Bitcoin",
    "bitcoin",
    "btc",
]

# Market refresh interval in seconds
MARKET_REFRESH_INTERVAL = int(os.getenv("MARKET_REFRESH_INTERVAL", "60"))

# Candle timeframe for analysis (in minutes)
CANDLE_TIMEFRAME_MINUTES = int(os.getenv("CANDLE_TIMEFRAME_MINUTES", "5"))


# =============================================================================
# Retry Settings
# =============================================================================

# Maximum number of retries for failed API requests
MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))

# Initial delay between retries in seconds
INITIAL_RETRY_DELAY = float(os.getenv("INITIAL_RETRY_DELAY", "1.0"))

# Multiplier for exponential backoff
RETRY_BACKOFF_MULTIPLIER = float(os.getenv("RETRY_BACKOFF_MULTIPLIER", "2.0"))


# =============================================================================
# Logging Settings
# =============================================================================

# Log file path
LOG_FILE = os.getenv("LOG_FILE", "trading_log.txt")

# Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
