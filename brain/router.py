# brain/router.py
"""
SHOPZOO AI - Agent Router
------------------------
User चा input + intent पाहून
कोणता agent वापरायचा ते ठरवतो.
"""

from brain.identity import get_identity

# ===== Trading Agents =====
from agents.trading_agent import build_trading_algo
from agents.strategy_agent import analyze_strategy
from agents.codegen_agent import generate_python_algo
from agents.mql5_codegen_agent import generate_mql5_ea

# ===== Website Agent =====
from agents.codegen_agent import generate_website_html_css


class AgentRouter:
    def __init__(self):
        self.identity = get_identity()

    # ================= CORE ROUTING =================

    def route(self, intent: dict, user_input: str) -> dict:
        """
        Main routing function
        """
        domain = intent.get("domain")

        # Safety: domain missing
        if not domain:
            return self._unknown()

        # Check if AI supports this domain
        if not self.identity.is_domain_supported(domain):
            return self._unsupported(domain)

        # ================= TRADING =================
        if domain == "trading":
            return self._handle_trading(intent, user_input)

        # ================= WEBSITE BUILDER =================
        if domain == "website_builder":
            return self._handle_website_builder(intent)

        # ================= CSC =================
        if domain == "csc_services":
            return self._handle_csc(intent)

        # ================= BUSINESS / ERP =================
        if domain in ["business_automation", "office_erp"]:
            return self._handle_business(intent)

        # ================= FALLBACK =================
        return self._unknown()

    # ================= HANDLERS =================

    def _handle_trading(self, intent: dict, user_input: str) -> dict:
        """
        Trading related routing
        """
        result = {
            "domain": "trading",
            "steps": [],
            "outputs": {}
        }

        # Strategy Intelligence
        strategy = analyze_strategy(user_input)
        result["steps"].append("strategy_analysis")
        result["outputs"]["strategy"] = strategy

        # Algo Blueprint
        algo = build_trading_algo(intent)
        result["steps"].append("algo_blueprint")
        result["outputs"]["algo"] = algo

        # Python Algo Code
        python_code = generate_python_algo(algo, strategy)
        result["steps"].append("python_algo_generated")
        result["outputs"]["python_code"] = python_code

        # MQL5 EA Code
        mql5_code = generate_mql5_ea(algo, strategy)
        result["steps"].append("mql5_ea_generated")
        result["outputs"]["mql5_code"] = mql5_code

        return result

    def _handle_website_builder(self, intent: dict) -> dict:
        """
        Website Builder Agent Routing
        """
        result = {
            "domain": "website_builder",
            "steps": [],
            "outputs": {}
        }

        params = intent.get("params", {})

        # Business name (from intent)
        business = params.get("business", "My Business")

        # Theme
        theme = intent.get("theme", "blue")

        # Generate Website Code
        website_code = generate_website_html_css(
            business=business,
            theme=theme
        )

        result["steps"].append("website_generated")
        result["outputs"]["website"] = website_code

        return result

    def _handle_csc(self, intent: dict) -> dict:
        """
        CSC services placeholder
        """
        return {
            "domain": "csc_services",
            "message": "CSC Agent लवकरच activate होईल",
            "intent": intent
        }

    def _handle_business(self, intent: dict) -> dict:
        """
        Business / ERP placeholder
        """
        return {
            "domain": "business_automation",
            "message": "Business/ERP Agent लवकरच activate होईल",
            "intent": intent
        }

    # ================= FALLBACKS =================

    def _unsupported(self, domain: str) -> dict:
        return {
            "error": True,
            "message": f"Domain '{domain}' सध्या समर्थित नाही",
        }

    def _unknown(self) -> dict:
        return {
            "error": True,
            "message": "मी हे काम अजून शिकलेलो नाही",
        }


# ================= HELPER =================

def get_router() -> AgentRouter:
    """
    Router singleton getter
    """
    return AgentRouter()
