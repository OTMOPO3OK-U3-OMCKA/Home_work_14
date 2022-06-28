from sql_file import SQLConnector
v = SQLConnector()


def aaa7(one_type, release_year, genre):
    _SQL = f"""
    SELECT title, description
    FROM netflix
    WHERE type == '{one_type}'
    AND release_year == '{release_year}'
    AND listed_in LIKE '%{genre}%'
    """
    return v.aaa1(_SQL)


one_type = "Movie"
year = 1998
genre = "Dramas"
list_films = []
my_films = aaa7(one_type, str(year), genre)

for i in my_films:
    list_films.append({
        "title": i[0],
        "description": i[1]
    })

print(list_films)