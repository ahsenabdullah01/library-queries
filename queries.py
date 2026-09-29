
import sqlite3

conn = sqlite3.connect("library.db")
cur = conn.cursor()

# Part A: Books with price greater than Rs. 1000
print("Books above Rs.1000 (sorted):")

cur.execute("""
SELECT title, price
FROM books
WHERE price > 1000
ORDER BY price DESC;
""")

for row in cur.fetchall():
    print(row)


# Part B: Using AS to rename title
print("\nBooks with aliased title:")

cur.execute("""
SELECT title AS book_title, price
FROM books;
""")

for row in cur.fetchall():
    print(row)


# Part C: Fiction books with low stock
print("\nLow-stock Fiction books:")

cur.execute("""
SELECT title, genre, price, stock
FROM books
WHERE genre = 'Fiction'
AND stock < 5;
""")

for row in cur.fetchall():
    print(row)

conn.close()
