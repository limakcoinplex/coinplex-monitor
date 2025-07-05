
import datetime
import json
import random
import matplotlib.pyplot as plt

now = datetime.datetime.now()
date = now.strftime('%Y-%m-%d')
time = now.strftime('%H:%M:%S')

# Symulowane ceny
dates = [f"2025-07-{str(i).zfill(2)}" for i in range(1, 6)]
prices = [round(random.uniform(0.01, 0.05), 4) for _ in range(5)]

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

# Wczytanie alertu
try:
    with open("alerts.json") as f:
        alert = json.load(f)
        alert_status = alert.get("status", "inactive")
        alert_msg = alert.get("message", "")
except Exception:
    alert_status = "inactive"
    alert_msg = ""

# Generowanie HTML
with open("index.html", "w") as f:
    f.write(f"""<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Coinplex Monitor</title>
    <style>
        body {{ background-color: #111; color: #eee; font-family: sans-serif; padding: 20px; }}
        .alert {{ background: #300; color: #f66; padding: 10px; border: 1px solid red; margin: 20px 0; }}
        .status-box {{ background: #222; padding: 15px; border-left: 5px solid orange; }}
    </style>
</head>
<body>
    <h1>🪙 CPLX</h1>
    <p>Ostatnia aktualizacja: <b>{date} {time}</b></p>
    {f'<div class="alert">{alert_msg}</div>' if alert_status == 'active' else ''}
    <div class='status-box'>
        <b>STATUS:</b> Token CPLX nadal bez ceny rynkowej<br>
        <b>OSTRZEŻENIE:</b> Brak aktywnych giełd, token w fazie zamkniętej emisji.
    </div>
    <h2>Symulowany wykres CPLX</h2>
    <img src="chart.png" width="100%" />
    <h3>Twoja inwestycja</h3>
    <p>Kwota zainwestowana: <b>1000 USD</b></p>
    <p>Możliwość wypłaty: <i>Brak w tej chwili</i></p>
</body>
</html>""")
