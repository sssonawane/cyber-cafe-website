def understand_intent(user_input: str) -> dict:
    text = user_input.lower()

    intent = {
        "type": "unknown",
        "domain": None,
        "params": {}
    }

    if "algo" in text or "trading" in text:
        intent["type"] = "create_algo"
        intent["domain"] = "trading"

        for word in text.split():
            if word.endswith("%"):
                intent["params"]["risk"] = word

    return intent
from .trading_agent import build_trading_algo
from .trading_agent import build_trading_algo
from .strategy_agent import analyze_strategy
from .trading_agent import build_trading_algo
from .strategy_agent import analyze_strategy
from .trading_agent import build_trading_algo
from .strategy_agent import analyze_strategy
from .codegen_agent import generate_python_algo
from .trading_agent import build_trading_algo
from .strategy_agent import analyze_strategy
from .codegen_agent import generate_python_algo
from .mql5_codegen_agent import generate_mql5_ea
