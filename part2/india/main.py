import sqlite3


def main():
    con = sqlite3.connect("../netflix.db")
    cur = con.cursor()
    sqlite_query = """
    SELECT type, count(type)
    FROM netflix
    WHERE country = 'India'
    GROUP BY type
    """
    cur.execute(sqlite_query)
    # здесь должно быть формирование и вывод списка
    # print(cur.fetchall())
    for i in cur.fetchall():
        if i[0] == 'Movie':
            print(f'фильмы: {i[1]} шт')
        if i[0] == 'TV Show':
            print(f'сериалы: {i[1]} шт')
    con.close()


if __name__ == '__main__':
    main()
