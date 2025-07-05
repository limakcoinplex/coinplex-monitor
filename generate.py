import datetime
import random
import matplotlib.pyplot as plt

# Aktualna data i godzina
now = datetime.datetime.now()
date = now.strftime('%Y-%m-%d')
time = now.strftime('%H:%M:%S')

# Symulacja cen
dates = [f"2025-07-{str(i).zfill(2)}" for i in range(1, 6)]
prices = [round(random.uniform(0.01, 0.05), 4) for _ in range(5)]

# Wykres
plt.figure(figsize=(6, 3))
plt.plot(dates, prices, marker='o', color='orange')
plt.title('Symulowany wykres ceny CPLX')
plt.xlabel('Data')
plt.ylabel('Cena (USD)')
plt.grid(True)
plt.tight_layout()
plt.savefig("chart.png")

# HTML
html = f"""
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CPLX Monitor</title>
    <style>
        body {{
        <p>Ostatnia aktualizacja: {date} {time}</p>
            background-color: #111;
            color: white;
            font-family: Arial, sans-serif;
            padding: 20px;
        }}
        .status {{
            border-left: 5px solid orange;
            padding: 10px;
            background-color: #222;
            margin-bottom: 20px;
        }}
        .status span {{
            color: red;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <h1>CPLX</h1>
    <p>Ostatnia aktualizacja: <strong>{date} {time}</strong></p>

    <div class="status">
        <p><span>STATUS:</span> Token CPLX nadal bez ceny rynkowej (0 USD).</p>
        <p><span>OSTRZEŻENIE:</span> Brak aktywnych giełd, token w fazie zamkniętej emisji.</p>
    </div>

    <h2>Symulowany wykres CPLX</h2>
    <img src="chart.png" alt="Wykres CPLX" width="100%">

    <h2>Twoja inwestycja</h2>
    <p>Kwota zainwestowana: <strong>1000 USD</strong></p>
    <p>Możliwość wypłaty: <em>Brak w tej chwili</em></p>

    <h2>Monitoring</h2>
    <ul>
        <li>Cena CPLX (obecnie 0 USD)</li>
        <li>Automatyczne alerty bezpieczeństwa (w przygotowaniu)</li>
        <li>Codzienne sprawdzanie statusu tokena</li>
    </ul>
</body>
</html>
"""

# Zapisz HTML
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

# Dodaj ukryty komentarz, by GitHub widział zmianę
with open("index.html", "a", encoding="utf-8") as f:
    f.write(f"\n<!-- update: {datetime.datetime.now()} -->")
