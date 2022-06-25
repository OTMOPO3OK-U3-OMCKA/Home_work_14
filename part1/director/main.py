import sqlite3


def main():
    con = sqlite3.connect("../netflix.db")
    cur = con.cursor()
    sqlite_query = """
    SELECT director
    FROM netflix
    WHERE director != ''
    """
    cur.execute(sqlite_query)
    # здесь должно быть формирование и вывод списка
    hh =[]
    for i in cur.fetchall():
        gg = i[0].split(', ')
        hh = hh + (gg)

    for i in set(hh):
        print(f"* {i}")

    con.close()


if __name__ == '__main__':
    main()
