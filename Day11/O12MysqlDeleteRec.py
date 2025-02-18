
import pymysql

conn = pymysql.connect(host='localhost',  user='root', password="", database= 'playersdb', port=3306)

cursor = conn.cursor()

query = "delete from player where plyid = 3"

cursor.execute(query)

conn.commit()
cursor.close()
conn.close()