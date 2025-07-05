import datetime
import json
import random
import matplotlib.pyplot as plt

# Aktualna data i godzina
now = datetime.datetime.now()
date = now.strftime('%Y-%m-%d')
time = now.strftime('%H:%M:%S')

# Symulowane ceny (losowe)
dates = [f"2025-07-0{d}" for d in range(1, 6)]
prices = [round(random.uniform(0.01, 0.05), 4) for _ in dates]

# Generowanie wykresu
plt.figure(figsize=(6, 3))
plt.plot(dates, prices, marker='o', color='orange')
plt.title('Symulowany wykres ceny CPLX')
plt.xlabel('Data')
plt.ylabel('Cena (USD)')
plt.grid(True)
plt.tight_layout()
plt.savefig("chart.png")
plt.close()

# Tworzenie pliku HTML z dynamicznymi danymi
with open("index.html", "w", encoding="utf-8") as f:
    f.write(f"""
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Coinplex Monitor</title>
    <style>
        body {{
            background-color: #121212;
            color: #fff;
            font-family: Arial, sans-serif;
            padding: 20px;
        }}
        .status {{
            padding: 10px;
            background-color: #333;
            border-left: 5px solid orange;
            margin-bottom: 20px;
        }}
    </style>
</head>
<body>
    <h1>📊 Coinplex Monitor</h1>
    <p>Ostatnia aktualizacja: <strong>{date} {time}</strong></p>

    <div class="status">
        <p><strong>STATUS:</strong> Token CPLX nadal bez ceny rynkowej (0 USD).</p>
        <p><strong>OSTRZEŻENIE:</strong> Brak aktywnych giełd, token w fazie zamkniętej emisji.</p>
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

    <!-- Ukryty komentarz: {random.randint(1,1000000)} -->
</body>
</html>
    """)
