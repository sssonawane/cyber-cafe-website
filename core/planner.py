def make_plan(intent: dict) -> list:
    if intent.get("type") == "create_algo":
        return [
            "Define trading strategy",
            "Set risk management rules",
            "Select market and timeframe",
            "Build algorithm logic",
            "Prepare backtesting"
        ]
    return []
