import sqlite3


def main():
    con = sqlite3.connect("../netflix.db")
    cur = con.cursor()
    sqlite_query = """
    SELECT title, release_year
    FROM netflix
    WHERE release_year BETWEEN 1943 AND 1945
    """
    cur.execute(sqlite_query)
    # здесь должно быть формирование и вывод списка
    for i in cur.fetchall():
        print(f'{i[0]} - {i[1]}')
    # print(cur.fetchall())
    con.close()


if __name__ == '__main__':
    main()
