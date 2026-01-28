# main.py
"""
SHOPZOO AI - Autonomous Brain Integrated Entry Point
----------------------------------------------------
User → Intent → Governor → Router → Codegen → Output
"""

import os
import sys

# ================= CORE =================
from core.intent import understand_intent
from core.planner import make_plan
from core.reasoner import reason
from core.memory import save_memory

# ================= BRAIN =================
from brain.identity import get_identity
from brain.router import get_router
from brain.decision import get_decision_engine
from brain.governor import get_governor


OUTPUT_DIR = "_outputs"


# ==================================================
# SAVE WEBSITE FILES (SINGLE + MULTI PAGE)
# ==================================================

def save_website_files(website_data: dict):
    """
    Save generated website files to _outputs folder
    Supports:
    - Single page (html + css)
    - Multi page (pages + css)
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # ---------- Multi-page ----------
    if "pages" in website_data:
        pages = website_data.get("pages", {})
        for filename, html in pages.items():
            with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
                f.write(html)

        with open(os.path.join(OUTPUT_DIR, "style.css"), "w", encoding="utf-8") as f:
            f.write(website_data.get("css", ""))

        return os.path.join(OUTPUT_DIR, "index.html")

    # ---------- Single-page ----------
    html_path = os.path.join(OUTPUT_DIR, "website.html")
    css_path = os.path.join(OUTPUT_DIR, "style.css")

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(website_data.get("html", ""))

    with open(css_path, "w", encoding="utf-8") as f:
        f.write(website_data.get("css", ""))

    return html_path


# ==================================================
# MAIN LOOP
# ==================================================

def main():
    # -------- Debug Info --------
    print("🐍 Python:", sys.executable)
    print("📂 Project Dir:", os.getcwd())
    print("-" * 60)

    # -------- Init Brain --------
    identity = get_identity()
    router = get_router()
    decision_engine = get_decision_engine()
    governor = get_governor()

    print("🤖 SHOPZOO AI started")
    print(f"🧠 Identity: {identity.name} v{identity.version}")
    print("Type 'exit' to quit")
    print("-" * 60)

    while True:
        user_input = input("You ➜ ")

        if user_input.lower() == "exit":
            print("👋 SHOPZOO AI बंद होत आहे")
            break

        # ================= PIPELINE =================

        # 1️⃣ Intent
        intent = understand_intent(user_input)
        print("🧪 INTENT ➜", intent)

        # 2️⃣ Plan + Reason
        plan = make_plan(intent)
        _ = reason(plan)

        # 3️⃣ Memory
        save_memory(user_input, intent)

        # 4️⃣ Governor
        gov_check = governor.validate(intent)
        print("🧪 GOVERNOR ➜", gov_check)

        if not gov_check.get("allowed"):
            print("🛑 Action blocked by Governor")
            print("Reason:", gov_check.get("reason"))
            print("-" * 60)
            continue

        # 5️⃣ Router
        routed_output = router.route(intent, user_input)
        print("🧪 ROUTER ➜", routed_output)

        # 6️⃣ Decision
        final_response = decision_engine.decide(routed_output)

        # ================= OUTPUT =================

        print("\n✅ AI RESPONSE")

        # ---------- WEBSITE BUILDER ----------
        if routed_output.get("domain") == "website_builder":
            website_data = routed_output.get("outputs", {}).get("website")

            if website_data:
                entry_file = save_website_files(website_data)

                print("🌐 Website Generated Successfully!")
                print(f"📄 Open: {entry_file}")
                print("➡️ Browser मध्ये open करण्यासाठी:")
                print(f"   start {entry_file}")

            else:
                print("❌ Website generation failed")

        # ---------- OTHER DOMAINS ----------
        else:
            for key, value in final_response.items():
                print(f"{key}: {value}")

        print("-" * 60)


# ================= ENTRY =================

if __name__ == "__main__":
    main()
