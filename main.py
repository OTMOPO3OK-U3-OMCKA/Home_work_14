import sqlite3

_SQL = """
SELECT *
FROM netflix
WHERE title = '100 Meters'
"""

with sqlite3.connect("netflix.db") as con:
    cur = con.cursor()
    cur.execute(_SQL)


for i in cur.fetchall():
    print(i)
