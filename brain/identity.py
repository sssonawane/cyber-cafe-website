# brain/identity.py
"""
SHOPZOO AI - Identity Module
---------------------------
AI कोण आहे, काय करू शकतो,
कोणते domains supported आहेत
ते इथे define केलं आहे.
"""

class AIIdentity:
    def __init__(self):
        # ================= BASIC INFO =================
        self.name = "SHOPZOO AI"
        self.version = "1.0"

        # ================= SUPPORTED DOMAINS =================
        # ⚠️ Governor आणि Router हे इथेच पाहतात
        self.supported_domains = {
            "trading",
            "csc_services",
            "business_automation",
            "office_erp",
            "website_builder"   # 🔥 WEBSITE BUILDER ENABLED
        }

    def is_domain_supported(self, domain: str) -> bool:
        """
        Check if domain is supported by AI identity
        """
        if not domain:
            return False
        return domain in self.supported_domains


# ================= HELPER =================

_identity_instance = None

def get_identity() -> AIIdentity:
    """
    Singleton Identity Getter
    """
    global _identity_instance
    if _identity_instance is None:
        _identity_instance = AIIdentity()
    return _identity_instance
