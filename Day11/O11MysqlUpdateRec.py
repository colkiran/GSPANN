
import pymysql

conn = pymysql.connect(host='localhost',  user='root', password="", database= 'playersdb', port=3306)

cursor = conn.cursor()

query = "update player set plyname = 'Pusarla Venkata Sindhu' where plyid = 5"

cursor.execute(query)

conn.commit()
cursor.close()
conn.close()
