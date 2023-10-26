import pymysql

conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="zjl195834", charset="utf8",
                       database="pymysql")
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

cursor.execute("update admin set mobile=%s where id=%s ", ["213dsad",3,])
conn.commit()

cursor.close()
conn.close()
