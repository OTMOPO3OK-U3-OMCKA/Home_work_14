import sqlite3


def main():
    con = sqlite3.connect("../netflix.db")
    cur = con.cursor()
    sqlite_query = """
    SELECT title, "cast"
    FROM netflix
    WHERE director LIKE '%Guy Ritchie%'
    """
    cur.execute(sqlite_query)
    for i in cur.fetchall():
        print(f'* {i[0]} : {i[1]}')
    # здесь должно быть формирование и вывод списка
    # print(cur.fetchall())
    con.close()


if __name__ == '__main__':
    main()
