import mysql.connector
from mysql.connector import errorcode


class hentOppslag:

    def __init__(self) -> None:
        dbconfig = {'host': 'kark.uit.no',
                    'user': 'stud_v22_jakobsenmal',
                    'password': 'ylaFCMMb0tsmgyxF',
                    'database': 'stud_v22_jakobsenmal', }
        self.configuration = dbconfig

    def __enter__(self) -> 'cursor':
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor(prepared=True)
        return self

    def __exit__(self, exc_type, exc_val, exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def query(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def visAlle(self):
        try:
            self.cursor.execute("SELECT * FROM Oppslag")
            result = self.cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print(err)

    def visKategori(self, kat_id):
        try:
            self.cursor.execute("SELECT * FROM Kategori ORDER BY kat_id")
            result = self.cursor.fetchone()
            return result
        except mysql.connector.Error as err:
            print(err)