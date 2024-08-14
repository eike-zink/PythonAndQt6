# Beispiel für ein Daten-Visualierungsprogramm

Grundlage: https://doc.qt.io/qtforpython-6/tutorials/datavisualize/index.html


Daten: 

https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson

oder 

https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.csv


## Beispiel zum Auslesen von Daten über einen einfachen Web-Services

### JSON-Datei
``` python 
import urllib.request, json 
with urllib.request.urlopen("http://maps.googleapis.com/maps/api/geocode/json?address=google") as url:
    data = json.load(url)
    print(data)
```

### CSV-Datei

``` python
import csv
import urllib2

url = 'http://winterolympicsmedals.com/medals.csv'
response = urllib2.urlopen(url)
cr = csv.reader(response)

for row in cr:
    print row
```

``` python
import csv, urllib.request

url = 'http://winterolympicsmedals.com/medals.csv'
response = urllib.request.urlopen(url)
lines = [l.decode('utf-8') for l in response.readlines()]
cr = csv.reader(lines)

for row in cr:
    print(row)
```

### Panda

``` python
import pandas as pd
data = pd.read_csv('https://example.com/passkey=wedsmdjsjmdd')
```