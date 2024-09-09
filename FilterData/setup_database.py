import sqlite3
import random

# Verbindung zur SQLite-Datenbank herstellen (oder erstellen, falls sie noch nicht existiert)
connection = sqlite3.connect("books.db")
cursor = connection.cursor()

# Tabelle erstellen
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        author TEXT NOT NULL,
        title TEXT NOT NULL,
        location TEXT NOT NULL,
        year INTEGER NOT NULL,
        isbn TEXT NOT NULL
    )
''')

# Beispiel-Daten für Autoren, Orte und Buchtitel
authors = ['Alice Walker', 'George Orwell', 'J.K. Rowling', 'Ernest Hemingway', 'Jane Austen']
titles = ['The Color Purple', '1984', 'Harry Potter', 'The Old Man and the Sea', 'Pride and Prejudice']
locations = ['New York', 'London', 'Paris', 'Berlin', 'Tokyo']


# Zufällige Testdaten generieren und in die Tabelle einfügen
def generate_isbn():
    """Generiert eine zufällige ISBN-Nummer"""
    return f"{random.randint(1000000000, 9999999999)}"


for _ in range(1000):  # 1000 Testdatensätze erstellen
    author = random.choice(authors)
    title = random.choice(titles)
    location = random.choice(locations)
    year = random.randint(1900, 2023)
    isbn = generate_isbn()

    cursor.execute('''
        INSERT INTO books (author, title, location, year, isbn)
        VALUES (?, ?, ?, ?, ?)
    ''', (author, title, location, year, isbn))

# Änderungen speichern und Verbindung schließen
connection.commit()
connection.close()

print("Testdaten wurden erfolgreich erstellt!")
