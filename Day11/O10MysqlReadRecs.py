
import pymysql
from prettytable import from_db_cursor

conn = pymysql.connect(host='localhost',  user='root', password="", database= 'playersdb', port=3306)

cursor = conn.cursor()

cursor.execute("select * from player")

prtyTbl = from_db_cursor(cursor)

cursor.close()

prtyTbl.align['plyname'] = 'l'
prtyTbl.align['sport'] = 'l'
prtyTbl.align['acheivement'] = 'l'

print(prtyTbl)
