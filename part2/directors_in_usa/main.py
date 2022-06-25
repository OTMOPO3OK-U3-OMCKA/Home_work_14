import sqlite3


def main():
    con = sqlite3.connect("../netflix.db")
    cur = con.cursor()
    sqlite_query = """
    SELECT director, count(director)
    FROM netflix
    WHERE country LIKE 'United States'
    AND director != ''
    GROUP BY director
    """
    cur.execute(sqlite_query)
    # здесь должно быть формирование и вывод списка
    # print(cur.fetchall())
    for i in cur.fetchall():
        print(f'* {i[0]} : {i[1]} фильмов')
    con.close()


if __name__ == '__main__':
    main()
