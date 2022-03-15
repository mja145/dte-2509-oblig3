import mysql.connector

dbconfig = { 'host' : kark.uit.no',
    'user' = 'stud_v22_jakobsenmal',
    'password': 'ylaFCMMb0tsmgyxF',
    'database': 'stud_v22_jakobsenmal', }
conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()
_SQL = """SELECT * FROM stud_v22_jakobsenmal;
cursor.execute(_SQL)
result = cursor.fetchall()
return render_template('index.html',
            students = result.cursor.close()
cursor.close()
conn.close()

FLASK_APP=app.py
FLASK_ENV=development