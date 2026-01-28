# agents/strategy_agent.py

def analyze_strategy(user_input: str) -> dict:
    text = user_input.lower()

    strategy = {
        "style": "intraday",
        "timeframe": "M15",
        "market": "forex"
    }

    if "scalp" in text:
        strategy["style"] = "scalping"
        strategy["timeframe"] = "M5"

    if "swing" in text:
        strategy["style"] = "swing"
        strategy["timeframe"] = "H1"

    if "gold" in text or "xauusd" in text:
        strategy["market"] = "XAUUSD"

    if "crypto" in text or "btc" in text:
        strategy["market"] = "crypto"

    return strategy
