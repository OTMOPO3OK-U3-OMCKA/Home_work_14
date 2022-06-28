import sqlite3


class SQLConnector:
    def aaa1(self, my_sql):
        with sqlite3.connect("netflix.db") as con:
            cur = con.cursor()
            cur.execute(my_sql)

        return cur.fetchall()

    def aaa2(self, film_name):
        _SQL = f"""
        SELECT title, country, release_year, listed_in, description
        FROM netflix
        WHERE title == '{film_name}'
        """
        my_film = self.aaa1(_SQL)
        if my_film:
            my_film_json = {
                "title": my_film[0][0],
                "country": my_film[0][1],
                "release_year": int(my_film[0][2]),
                "genre": my_film[0][3],
                "description": my_film[0][4].replace('\n', '')
            }
            return my_film_json

    def aaa3(self, year, year2):
        _SQL = f"""
        SELECT title, release_year
        FROM netflix
        WHERE release_year BETWEEN {year} AND {year2}
        LIMIT 100
        """
        my_films = self.aaa1(_SQL)
        list_my_films = []
        if my_films:
            for my_film in my_films:
                list_my_films.append({
                    "title": my_film[0],
                    "release_year": my_film[1]
                })

        return list_my_films

    def aaa4(self, rating):
        _SQL = f"""
        SELECT title, rating, description
        FROM netflix
        WHERE rating IN {rating}
        """
        list_my_films = []
        my_films = self.aaa1(_SQL)
        if my_films:
            for my_film in my_films:
                list_my_films.append({
                    "title": my_film[0],
                    "rating": my_film[1],
                    "description": my_film[2]
                })

        return list_my_films

    def aaa5(self, genre):
        _SQL = f"""
        SELECT title, description
        FROM netflix
        WHERE listed_in LIKE '%{genre}%'
        ORDER BY date_added DESC
        LIMIT 10
        """
        list_my_films = []
        my_films = self.aaa1(_SQL)
        if my_films:
            for my_film in my_films:
                list_my_films.append({
                    "title": my_film[0],
                    "description": my_film[1]
                })

        return list_my_films

    def aaa6(self, name1, name2):
        _SQL = f"""
        SELECT title, "cast"
        FROM netflix
        WHERE "cast" LIKE '%{name1}%'
        OR "cast" LIKE '%{name2}%'
        """
        my_films = self.aaa1(_SQL)
        act = {
            name1: [],
            name2: [],
        }
        ll = []
        if my_films:
            for i in my_films:
                ll.append({
                    "title": i[0],
                    "cast": i[1].split(', ')
                })
