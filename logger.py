"""
Logging module for Polymarket trading bot.

Provides structured logging with timestamps, trade logging, and error tracking.
All logs are saved to trading_log.txt.
"""

import logging
import sys
from datetime import datetime
from typing import Optional, Any
import traceback

from config import LOG_FILE, LOG_LEVEL


def setup_logger(name: str = "polymarket_bot") -> logging.Logger:
    """
    Set up and configure the main logger.

    Args:
        name: Name of the logger instance.

    Returns:
        Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, LOG_LEVEL.upper(), logging.INFO))

    # Prevent duplicate handlers if logger is already configured
    if logger.handlers:
        return logger

    # Create formatters
    detailed_formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # File handler - always log everything to file
    file_handler = logging.FileHandler(LOG_FILE, mode="a", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(detailed_formatter)
    logger.addHandler(file_handler)

    # Console handler - show info and above
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(detailed_formatter)
    logger.addHandler(console_handler)

    return logger


# Global logger instance
logger = setup_logger()


def log_action(action: str, details: Optional[dict[str, Any]] = None) -> None:
    """
    Log a general action with optional details.

    Args:
        action: Description of the action being performed.
        details: Optional dictionary of additional details to log.
    """
    message = f"ACTION: {action}"
    if details:
        detail_str = " | ".join(f"{k}={v}" for k, v in details.items())
        message += f" | {detail_str}"
    logger.info(message)


def log_trade(
    market_id: str,
    market_question: str,
    side: str,
    price: float,
    size: float,
    outcome: str,
    order_id: Optional[str] = None
) -> None:
    """
    Log a trade execution with all relevant details.

    Args:
        market_id: ID of the market traded.
        market_question: The market question/description.
        side: Trade side (YES or NO).
        price: Price at which the trade was executed.
        size: Size of the trade in USDC.
        outcome: Trade outcome (BUY or SELL).
        order_id: Optional order ID if available.
    """
    trade_line = (
        "=" * 80 + "\n"
        f"TRADE EXECUTED\n"
        f"{'=' * 80}\n"
        f"Timestamp: {datetime.now().isoformat()}\n"
        f"Market ID: {market_id}\n"
        f"Market: {market_question}\n"
        f"Side: {side}\n"
        f"Price: {price:.4f}\n"
        f"Size: {size:.2f} USDC\n"
        f"Outcome: {outcome}\n"
    )
    if order_id:
        trade_line += f"Order ID: {order_id}\n"
    trade_line += "=" * 80

    logger.info(trade_line)


def log_error(error: Exception, context: Optional[str] = None) -> None:
    """
    Log an error with full traceback.

    Args:
        error: The exception that occurred.
        context: Optional context string describing what was happening.
    """
    tb = traceback.format_exc()
    error_message = f"ERROR: {type(error).__name__}: {str(error)}"
    if context:
        error_message = f"{context} | {error_message}"
    logger.error(error_message)
    logger.debug(f"TRACEBACK:\n{tb}")


def log_market_scan(markets_found: int, markets_eligible: int) -> None:
    """
    Log the results of a market scan.

    Args:
        markets_found: Total number of markets found.
        markets_eligible: Number of markets that passed eligibility checks.
    """
    logger.info(
        f"MARKET SCAN | Found: {markets_found} | Eligible: {markets_eligible}"
    )


def log_signal(
    market_id: str,
    signal_type: str,
    candle_data: dict[str, Any],
    volume_data: dict[str, Any]
) -> None:
    """
    Log a trading signal detection.

    Args:
        market_id: ID of the market where signal was detected.
        signal_type: Type of signal (e.g., "GREEN_CANDLE_HIGH_VOLUME").
        candle_data: Dictionary with candle information.
        volume_data: Dictionary with volume information.
    """
    logger.info(
        f"SIGNAL: {signal_type} | Market: {market_id} | "
        f"Open: {candle_data.get('open', 'N/A')} | "
        f"Close: {candle_data.get('close', 'N/A')} | "
        f"Volume: {volume_data.get('current', 'N/A')} | "
        f"Avg Volume: {volume_data.get('average', 'N/A')}"
    )


def log_api_request(method: str, endpoint: str, params: Optional[dict] = None) -> None:
    """
    Log an API request.

    Args:
        method: HTTP method used.
        endpoint: API endpoint called.
        params: Optional request parameters.
    """
    msg = f"API REQUEST: {method} {endpoint}"
    if params:
        msg += f" | Params: {params}"
    logger.debug(msg)


def log_api_response(status_code: int, response_time_ms: float, success: bool) -> None:
    """
    Log an API response.

    Args:
        status_code: HTTP status code received.
        response_time_ms: Response time in milliseconds.
        success: Whether the request was successful.
    """
    status = "SUCCESS" if success else "FAILED"
    logger.debug(
        f"API RESPONSE: {status} | Status: {status_code} | Time: {response_time_ms:.2f}ms"
    )
