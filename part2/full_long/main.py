import sqlite3


def main():
    con = sqlite3.connect("../netflix.db")
    cur = con.cursor()
    sqlite_query = """
    SELECT sum(duration)
    FROM netflix
    WHERE type = 'Movie'
    AND release_year > 2009
    """
    cur.execute(sqlite_query)
    # здесь должно быть формирование и вывод списка
    # print(cur.fetchall())
    our_time = round(cur.fetchall()[0][0]/60)
    print(f'Чтобы посмотреть все фильмы, нам нужно {our_time} часов.')
    con.close()


if __name__ == '__main__':
    main()
