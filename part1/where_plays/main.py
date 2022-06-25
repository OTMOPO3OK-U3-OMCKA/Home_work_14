import sqlite3


def main():
    con = sqlite3.connect("../netflix.db")
    cur = con.cursor()
    sqlite_query = """
    SELECT title, type
    FROM netflix
    WHERE netflix.cast LIKE '%Renée Zellweger%'
    AND type = 'TV Show'
    
    """
    cur.execute(sqlite_query)
    # здесь должно быть формирование и вывод списка
    # print(cur.fetchall())
    for i in cur.fetchall():
        print(i[0])
    con.close()


if __name__ == '__main__':
    main()
