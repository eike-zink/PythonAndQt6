# Beispiel für ein Daten-Visualierungsprogramm

Grundlage: https://doc.qt.io/qtforpython-6/tutorials/datavisualize/index.html

Daten: https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.csv

## Beispiel zum Auslesen von Daten über eine einfache URL-Abfrage

### CSV-Datei

``` python
import csv, urllib.request

url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.csv'
response = urllib.request.urlopen(url)
lines = [l.decode('utf-8') for l in response.readlines()]
cr = csv.reader(lines)

for row in cr:
    print(row)
```

### Panda

``` python
import pandas as pd
data = pd.read_csv('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.csv')
```