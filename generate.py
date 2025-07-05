
import matplotlib.pyplot as plt
from datetime import datetime
import base64
from io import BytesIO
import json
import random

# Wczytanie alertu
alert_message = ""
try:
    with open("alerts.json", "r") as alert_file:
        alert_data = json.load(alert_file)
        if alert_data.get("status") == "active":
            alert_message = alert_data.get("message", "")
except:
    alert_message = ""

# Symulacja zmieniającej się ceny CPLX (między 0 a 0.05 USD)
dates = ["2025-07-01", "2025-07-02", "2025-07-03", "2025-07-04", datetime.now().strftime('%Y-%m-%d')]
prices = [round(random.uniform(0.01, 0.03), 4) for _ in dates]

# Generowanie wykresu
plt.figure(figsize=(8, 4))
plt.plot(dates, prices, marker='o', color='orange')
plt.title('Wykres ceny CPLX (symulacja)')
plt.xlabel('Data')
plt.ylabel('Cena (USD)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Konwersja wykresu do base64
img_buffer = BytesIO()
plt.savefig(img_buffer, format='png')
img_buffer.seek(0)
img_base64 = base64.b64encode(img_buffer.read()).decode('utf-8')
plt.close()

# HTML z alertem i wykresem
html_content = f"""<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Monitor Coinplex – Limaklee</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #121212;
            color: #f0f0f0;
            margin: 0;
            padding: 20px;
        }}
        .container {{
            max-width: 900px;
            margin: auto;
            background-color: #1e1e1e;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(255,255,255,0.1);
        }}
        h1 {{
            color: #00ccff;
        }}
        .status {{
            padding: 10px;
            background: #333333;
            border-left: 6px solid #ffaa00;
            margin: 15px 0;
        }}
        .alert {{
            background-color: #660000;
            color: #fff;
            padding: 15px;
            margin: 15px 0;
            border-left: 6px solid red;
            font-weight: bold;
        }}
        footer {{
            margin-top: 30px;
            font-size: 0.9em;
            color: #888;
            text-align: center;
        }}
        img {{
            max-width: 100%;
            height: auto;
            margin-top: 20px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Monitor Coinplex – CPLX</h1>
        <p>Ostatnia aktualizacja: <strong>{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</strong></p>

        {f'<div class="alert">{alert_message}</div>' if alert_message else ''}

        <div class="status">
            <p><strong>STATUS:</strong> Token CPLX nadal nie ma oficjalnej ceny rynkowej.</p>
            <p><strong>UWAGA:</strong> Poniższy wykres oparty jest na danych symulowanych.</p>
        </div>

        <h3>Wykres CPLX</h3>
        <img src="data:image/png;base64,{img_base64}" alt="Wykres ceny CPLX">

        <h3>Twoja inwestycja</h3>
        <p>Kwota zainwestowana: <strong>1000 USD</strong></p>
        <p>Możliwość wypłaty: <em>Brak w tej chwili</em></p>

        <h3>Monitoring</h3>
        <ul>
            <li>Symulacja ceny CPLX (losowa, do czasu uruchomienia tokena)</li>
            <li>Alerty bezpieczeństwa z pliku alerts.json</li>
            <li>Automatyczna aktualizacja co godzinę</li>
        </ul>

        <footer>
            Stworzone przez <strong>Limaklee</strong> | Wersja LIVE symulowana
        </footer>
    </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)
