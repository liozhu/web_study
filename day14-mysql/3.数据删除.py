import pymysql

conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="zjl195834", charset="utf8",
                       database="pymysql")
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

sql = "delete from admin where id=2"
cursor.execute(sql)
conn.commit()

cursor.close()
conn.close()
