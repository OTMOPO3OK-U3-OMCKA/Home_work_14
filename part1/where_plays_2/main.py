import sqlite3


def main():
    con = sqlite3.connect("../netflix.db")
    cur = con.cursor()
    sqlite_query = """
    SELECT title, rating
    FROM netflix
    WHERE "cast" LIKE '%Joaquin Phoenix%'
    """
    cur.execute(sqlite_query)
    # здесь должно быть формирование и вывод списка
    # print(cur.fetchall())
    for i in cur.fetchall():
        print(f"* {i[0]} - {i[1]}")
    con.close()


if __name__ == '__main__':
    main()
