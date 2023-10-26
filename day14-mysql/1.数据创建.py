import pymysql

conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="zjl195834", charset="utf8",
                       database="pymysql")
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

sql = "insert into admin (username,passwd,mobile) values(%s,%s,%s)"
cursor.execute(sql,['sad','18sad23u1','21631723'])

sql = "insert into admin (username,passwd,mobile) values(%(n1)s,%(n2)s,%(n3)s)"
cursor.execute(sql,{"n1":'sasadd',"n2":'18sad23u1',"n3":'21631723'})

conn.commit()

cursor.close()
conn.close()
