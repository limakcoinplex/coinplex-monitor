
import matplotlib.pyplot as plt
from datetime import datetime
import base64
from io import BytesIO

# Przygotowanie danych (symulowane dane CPLX)
dates = ["2025-07-01", "2025-07-02", "2025-07-03", "2025-07-04", datetime.now().strftime('%Y-%m-%d')]
prices = [0.0] * len(dates)

# Generowanie wykresu
plt.figure(figsize=(8, 4))
plt.plot(dates, prices, marker='o', color='orange')
plt.title('Symulowany wykres ceny CPLX')
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

# Generowanie pliku HTML
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
        .tag {{
            font-weight: bold;
            color: #ff6666;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Monitor Coinplex – CPLX</h1>
        <p>Ostatnia aktualizacja: <strong>{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</strong></p>

        <div class="status">
            <p><span class="tag">STATUS:</span> Token CPLX nadal bez ceny rynkowej (0 USD).</p>
            <p><span class="tag">OSTRZEŻENIE:</span> Brak aktywnych giełd, token w fazie zamkniętej emisji.</p>
        </div>

        <h3>Symulowany wykres CPLX</h3>
        <img src="data:image/png;base64,{img_base64}" alt="Wykres ceny CPLX">

        <h3>Twoja inwestycja</h3>
        <p>Kwota zainwestowana: <strong>1000 USD</strong></p>
        <p>Możliwość wypłaty: <em>Brak w tej chwili</em></p>

        <h3>Monitoring</h3>
        <ul>
            <li>Cena CPLX (obecnie 0 USD)</li>
            <li>Automatyczne alerty bezpieczeństwa (w przygotowaniu)</li>
            <li>Codzienne sprawdzanie statusu tokena</li>
        </ul>

        <footer>
            Stworzone przez <strong>Limaklee</strong> | Tryb ciemny | ChatGPT 2025<br>
            Wersja z wykresem i automatyzacją (beta)
        </footer>
    </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)
