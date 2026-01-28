# brain/decision.py
"""
SHOPZOO AI - Decision Engine
----------------------------
Router कडून आलेल्या output वरून
AI अंतिम निर्णय घेतो:
- काय दाखवायचं
- काय सेव्ह करायचं
- काय पुढे execute करायचं
"""

import os
from datetime import datetime


class AIDecisionEngine:
    def __init__(self):
        self.log_dir = "ai_outputs"
        os.makedirs(self.log_dir, exist_ok=True)

    # ================= MAIN DECISION =================

    def decide(self, routed_output: dict) -> dict:
        """
        Central decision method
        """
        if routed_output.get("error"):
            return self._handle_error(routed_output)

        domain = routed_output.get("domain")

        if domain == "trading":
            return self._decide_trading(routed_output)

        if domain == "csc_services":
            return self._simple_message(routed_output)

        if domain == "business_automation":
            return self._simple_message(routed_output)

        return {
            "status": "unknown",
            "message": "निर्णय घेता आला नाही"
        }

    # ================= TRADING DECISIONS =================

    def _decide_trading(self, data: dict) -> dict:
        """
        Trading domain decision
        """
        outputs = data.get("outputs", {})
        steps = data.get("steps", [])

        response = {
            "status": "success",
            "domain": "trading",
            "summary": [],
            "files_saved": [],
            "next_actions": []
        }

        # Strategy summary
        if "strategy" in outputs:
            response["summary"].append("Strategy analysis completed")

        # Algo blueprint
        if "algo" in outputs:
            response["summary"].append("Trading algo blueprint created")

        # Save Python Algo
        if "python_code" in outputs:
            py_file = self._save_file(
                "generated_algo.py",
                outputs["python_code"]
            )
            response["files_saved"].append(py_file)

        # Save MQL5 EA
        if "mql5_code" in outputs:
            mq5_file = self._save_file(
                "generated_ea.mq5",
                outputs["mql5_code"]
            )
            response["files_saved"].append(mq5_file)

        # Suggested next actions
        response["next_actions"].extend([
            "Backtest using generated_algo.py",
            "Compile generated_ea.mq5 in MT5",
            "Run EA on DEMO account"
        ])

        return response

    # ================= HELPERS =================

    def _save_file(self, filename: str, content: str) -> str:
        """
        Save generated content to file
        """
        path = os.path.join(self.log_dir, filename)

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        return path

    def _handle_error(self, data: dict) -> dict:
        return {
            "status": "error",
            "message": data.get("message", "Unknown error")
        }

    def _simple_message(self, data: dict) -> dict:
        return {
            "status": "info",
            "domain": data.get("domain"),
            "message": data.get("message", "Process completed")
        }


# ================= HELPER =================

def get_decision_engine() -> AIDecisionEngine:
    """
    Decision engine singleton getter
    """
    return AIDecisionEngine()
