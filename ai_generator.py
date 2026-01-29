# ai_generator.py
from datetime import datetime

html = f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Cyber Cafe</title>
</head>
<body>
  <h1>Cyber Cafe</h1>
  <p>Updated by AI at {datetime.now()}</p>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Website updated by AI")
