# core/intent.py
"""
Intent Understanding Module
---------------------------
User input → intent (domain, type, params)
"""

def understand_intent(user_input: str) -> dict:
    # 🔥 DEBUG (आत्ता ठेव – नंतर काढू)
    print("🔥 INTENT FUNCTION CALLED WITH:", repr(user_input))

    if not user_input or not user_input.strip():
        return {
            "domain": None,
            "type": None,
            "params": {}
        }

    text = user_input.strip().lower()

    # ================= WEBSITE BUILDER =================
    if any(word in text for word in ["website", "वेबसाईट", "site", "page", "वेब"]):

        # ---- Business Detection ----
        business = "My Business"

        if "cyber" in text:
            business = "Cyber Cafe"
        elif "photo" in text or "studio" in text:
            business = "Photo Studio"
        elif "shop" in text or "store" in text or "दुकान" in text:
            business = "General Store"
        elif "office" in text:
            business = "Office"
        elif "school" in text or "class" in text:
            business = "Education Center"

        # ---- Theme Detection ----
        theme = "blue"
        if "green" in text or "हिरवा" in text:
            theme = "green"
        elif "red" in text or "लाल" in text:
            theme = "red"
        elif "dark" in text or "black" in text:
            theme = "dark"

        return {
            "domain": "website_builder",
            "type": "generate",
            "theme": theme,
            "params": {
                "business": business
            }
        }

    # ================= TRADING =================
    if any(word in text for word in ["trade", "trading", "strategy", "algo", "mt5", "ea"]):
        return {
            "domain": "trading",
            "type": "generate",
            "params": {}
        }

    # ================= CSC =================
    if any(word in text for word in ["csc", "service center", "government", "सेवा केंद्र"]):
        return {
            "domain": "csc_services",
            "type": "info",
            "params": {}
        }

    # ================= BUSINESS / ERP =================
    if any(word in text for word in ["erp", "billing", "invoice", "office software"]):
        return {
            "domain": "business_automation",
            "type": "generate",
            "params": {}
        }

    # ================= FALLBACK =================
    return {
        "domain": None,
        "type": None,
        "params": {}
    }
