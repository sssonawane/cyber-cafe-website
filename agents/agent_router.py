from agents.trading_agent import build_trading_algo
from agents.strategy_agent import analyze_strategy

def route_agents(user_input: str, intent: dict):
    result = {}

    # Strategy Intelligence
    strategy = analyze_strategy(user_input)
    result["strategy"] = strategy

    # Trading Agent
    if intent.get("type") == "create_algo" and intent.get("domain") == "trading":
        result["trading_algo"] = build_trading_algo(intent)

    return result
