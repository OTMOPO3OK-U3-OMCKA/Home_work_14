import sqlite3


def main():
    con = sqlite3.connect("../netflix.db")
    cur = con.cursor()
    sqlite_query = """
    SELECT sum(duration)
    FROM netflix
    WHERE type = 'TV Show'
    AND director LIKE '%Alastair Fothergill%'
    """
    cur.execute(sqlite_query)
    # здесь должно быть формирование и вывод списка
    # print(cur.fetchall())
    value = cur.fetchall()[0][0]
    print(f'Alastair Fothergill снял {value} сезонов сериалов.')
    con.close()


if __name__ == '__main__':
    main()
