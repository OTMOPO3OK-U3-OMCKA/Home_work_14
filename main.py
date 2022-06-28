from sql_file import SQLConnector
from flask import Flask
from flask import jsonify

app = Flask(__name__)

m = SQLConnector()


@app.route("/movie/<title>")
def movie(title):
    aa = m.aaa2(title)
    if type(aa) is dict:
        return jsonify(aa)
    return "такого фильма нет"


@app.route("/movie/<year>/to/<year2>")
def search(year, year2):
    aa = m.aaa3(year, year2)
    if aa:
        return jsonify(aa)
    return "таких фильмов не найдено"


@app.route("/rating/<rating>")
def ratinger(rating):
    adult = "('R', 'NC-17')"
    family = "('G', 'PG', 'PG-13')"
    children = "('G')"
    if rating == "adult":
        return jsonify(m.aaa4(adult))
    elif rating == "family":
        return jsonify(m.aaa4(family))
    elif rating == "children":
        return jsonify(m.aaa4(children))
    return "фильмы с такими рейтингами не найдены"


@app.route("/genre/<genre>")
def genre(genre):
    g = m.aaa5(genre)
    if g:
        return jsonify(g)
    return "фильмов с таким жанром не найдено"


app.run()
