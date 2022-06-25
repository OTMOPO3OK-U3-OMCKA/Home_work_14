import sqlite3


def main():
    con = sqlite3.connect("../netflix.db")
    cur = con.cursor()
    sqlite_query = """
    SELECT description
    FROM netflix
    WHERE description LIKE '% train'
    OR description LIKE 'Train %'
    OR description LIKE '% train %'"""
    cur.execute(sqlite_query)
    # здесь должно быть формирование и вывод списка
    for i in cur.fetchall():
        print(i[0].replace('\n', ''))
    # print(cur.fetchall())
    con.close()


if __name__ == '__main__':
    main()
