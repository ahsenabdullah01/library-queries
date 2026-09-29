import sqlite3

conn = sqlite3.connect("library.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS books")

cur.execute("""
CREATE TABLE books (
    book_id INTEGER PRIMARY KEY,
    title TEXT,
    genre TEXT,
    price INTEGER,
    stock INTEGER
)
""")

books = [
    (1, "Data Science Basics", "Technology", 1450, 10),
    (2, "Clean Code", "Technology", 1200, 8),
    (3, "The Silent Patient", "Fiction", 1350, 2),
    (4, "Python Programming", "Technology", 950, 12),
    (5, "The Alchemist", "Fiction", 850, 7),
    (6, "Atomic Habits", "Self Help", 1100, 4),
    (7, "Artificial Intelligence", "Technology", 1600, 6),
    (8, "1984", "Fiction", 900, 3)
]

cur.executemany("""
INSERT INTO books
(book_id, title, genre, price, stock)
VALUES (?, ?, ?, ?, ?)
""", books)

conn.commit()
conn.close()

print("library.db created successfully.")
