def build_trading_algo(intent: dict) -> dict:
    """
    Trading algorithm blueprint generator
    """

    algo = {
        "market": "Forex",
        "symbol": "Not specified",
        "strategy": "Price Action",
        "risk": intent.get("params", {}).get("risk", "1%"),
        "timeframe": "M15",
        "rules": []
    }

    # Basic rules
    algo["rules"].append("Trade only in active sessions")
    algo["rules"].append("Risk per trade = " + algo["risk"])
    algo["rules"].append("One trade at a time")
    algo["rules"].append("Use Stop Loss and Take Profit")

    return algo
