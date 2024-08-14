# Test für einen automatischen Download der CSV-Datei

import csv
import urllib.request

url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.csv'

response = urllib.request.urlopen(url)
lines = [l.decode('utf-8') for l in response.readlines()]
cr = csv.reader(lines)

for line in cr:
    print(line)
