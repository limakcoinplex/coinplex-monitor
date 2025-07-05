import datetime
import random
import matplotlib.pyplot as plt

# Data i godzina
now = datetime.datetime.now()
date_str = now.strftime('%Y-%m-%d')
time_str = now.strftime('%H:%M:%S')

# Dane do wykresu
dates = [f"2025-07-{str(i).zfill(2)}" for i in range(1, 6)]
prices = [round(random.uniform(0.01, 0.05), 4) for _ in range(5)]

# Tworzenie wykresu
plt.figure(figsize=(6, 3))
plt.plot(dates, prices, marker='o', color='orange')
plt.title("Symulowany wykres CPLX")
plt.xlabel("Data")
plt.ylabel("Cena (USD)")
plt.grid(True)
plt.tight_layout()
plt.savefig("chart.png")
plt.close()

# Tworzenie strony HTML
with open("index.html", "w", encoding="utf-8") as f:
    f.write(f"""<!DOCTYPE html>
<html lang='pl'>
<head>
  <meta charset='UTF-8'>
  <title>Coinplex Monitor</title>
  <style>
    body {{ background-color: #111; color: white; font-family: sans-serif; }}
    .container {{ max-width: 800px; margin: auto; padding: 20px; }}
    .status {{ border: 1px solid orange; background: #222; padding: 10px; }}
    .alert {{ color: red; font-weight: bold; }}
  </style>
</head>
<body>
<div class='container'>
  <h1>CPLX</h1>
  <p>Ostatnia aktualizacja: <strong>{date_str} {time_str}</strong></p>
  <div class='status'>
    <p><strong>STATUS:</strong> Token CPLX nadal bez ceny rynkowej.</p>
    <p class='alert'><strong>OSTRZEŻENIE:</strong> Brak aktywnych giełd.</p>
  </div>
  <h2>Wykres</h2>
  <img src='chart.png' style='width:100%' alt='Wykres CPLX'>
</div>
<!-- auto-refresh-{random.randint(1000,9999)} -->
</body>
</html>""")
