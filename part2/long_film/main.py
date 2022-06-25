import sqlite3


def main():
    con = sqlite3.connect("../netflix.db")
    cur = con.cursor()
    sqlite_query = """
    SELECT title, max(duration)
    FROM netflix
    WHERE type = 'Movie'
    """
    cur.execute(sqlite_query)
    # здесь должно быть формирование и вывод списка
    # print(cur.fetchall())
    value = cur.fetchall()[0]
    print(f'{value[0]} - {value[1]}')
    con.close()


if __name__ == '__main__':
    main()
