from flask import Flask, render_template, request, escape, redirect, request
import mysql.connector
from oppslag import Oppslag
from hentoppslag import hentOppslag

dbconfig = {'host': 'kark.uit.no',
            'user': 'stud_v22_jakobsenmal',
            'password': 'ylaFCMMb0tsmgyxF',
            'database': 'stud_v22_jakobsenmal', }

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=["GET"])
def index() -> 'html':
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = """SELECT * from oppslag group by dato DESC""";
    cursor.execute(_SQL)
    result = cursor.fetchall()
    return render_template('index.html', oppslag=result)


@app.route('/kategori=1', methods=["GET"])
def annonser() -> 'html':

    with hentOppslag() as db:
        result = db.visAlle()
    return render_template('annonser.html',
                           result=result)


@app.route('/kategori=2')
def csrf() -> 'html':
    return render_template('index.html')


@app.route('/kategori=3')
def diverse():
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = """SELECT * from oppslag group by dato DESC""";
    cursor.execute(_SQL)
    result = cursor.fetchall()
    return render_template('diverse.html', oppslag=result)


@app.route('/kategori=4')
def gjesteforelesning():
    return "gjesteforelesning"


@app.route('/kategori=5')
def kurs():
    return "kurs"


@app.route('/kategori=6')
def oppslag():
    return "oppslag"


if __name__ == '__main__':
    app.run(debug=True)
