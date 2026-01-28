# brain/governor.py
"""
SHOPZOO AI - Governor Module
----------------------------
हा module AI च्या actions वर नियंत्रण ठेवतो.
Risk, safety, permissions आणि blocks इथे ठरतात.
"""

from brain.identity import get_identity


class AIGovernor:
    def __init__(self):
        self.identity = get_identity()

        # 🔒 Hard Limits (Trading only)
        self.limits = {
            "max_risk_percent": 2,      # Absolute max risk
            "default_risk_percent": 1,  # Default safe risk
            "max_open_trades": 1,       # One trade at a time
            "allow_real_trading": False # DEMO only by default
        }

        # ✅ Safe non-trading domains (NO risk checks)
        self.safe_domains = {
            "website_builder",
            "csc_services",
            "business_automation",
            "office_erp"
        }

    # ================= CORE CHECK =================

    def validate(self, intent: dict, context: dict = None) -> dict:
        """
        AI action validate करतो
        """
        domain = intent.get("domain")
        action_type = intent.get("type")
        params = intent.get("params", {})

        # 🔴 Domain missing
        if not domain:
            return self._blocked("Domain missing or undefined")

        # 🔴 Domain not supported by identity
        if not self.identity.is_domain_supported(domain):
            return self._blocked(f"Domain '{domain}' not allowed")

        # ✅ SAFE DOMAINS (Website, CSC, Business)
        if domain in self.safe_domains:
            return {
                "allowed": True,
                "mode": "SAFE",
                "risk": 0
            }

        # ================= TRADING SAFETY =================

        # 🔴 Block real money trading
        if action_type == "real_money_trade":
            return self._blocked("Real money trading is disabled")

        # 🔴 Risk check (only for trading)
        risk = self._extract_risk(params)
        if risk > self.limits["max_risk_percent"]:
            return self._blocked(
                f"Risk {risk}% exceeds allowed limit ({self.limits['max_risk_percent']}%)"
            )

        # ✅ Trading allowed (DEMO)
        return {
            "allowed": True,
            "risk": risk,
            "mode": "DEMO"
        }

    # ================= HELPERS =================

    def _extract_risk(self, params: dict) -> int:
        """
        Risk % extract करतो
        """
        raw = params.get("risk", self.limits["default_risk_percent"])

        try:
            if isinstance(raw, str) and "%" in raw:
                return int(raw.replace("%", ""))
            return int(raw)
        except Exception:
            return self.limits["default_risk_percent"]

    def _blocked(self, reason: str) -> dict:
        """
        Block response
        """
        return {
            "allowed": False,
            "reason": reason
        }


# ================= HELPER =================

def get_governor() -> AIGovernor:
    """
    Governor singleton getter
    """
    return AIGovernor()
