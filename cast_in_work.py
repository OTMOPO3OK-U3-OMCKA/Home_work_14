from sql_file import SQLConnector
v = SQLConnector()


def aaa61(name):
    name_1 = []
    for film in my_films:
        act = film[0].split(', ')
        if name in act:
            name_1.extend(act)
    n_1 = set()
    for n in name_1:
        if n != name and name_1.count(n) > 2:
            n_1.add(n)
    return list(n_1)


def aaa62(name_1, name_2):
    _SQL = f"""
    SELECT "cast"
    FROM netflix
    WHERE "cast" LIKE '%{name_1}%'
    OR "cast" LIKE '%{name_2}%'
    """
    return v.aaa1(_SQL)

"""
Rose McIver и Ben Lamb, Jack Black и Dustin Hoffman
"""
name1 = "Rose McIver"
name2 = "Ben Lamb"

my_films = aaa62(name1, name2)
actor = {
    name1: aaa61(name1),
    name2: aaa61(name2),
}
print(actor)
