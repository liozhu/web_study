import pymysql

conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="zjl195834", charset="utf8",
                       database="pymysql")
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

cursor.execute("select * from admin")
data_list = cursor.fetchall()
for row_dict in data_list:
    print(row_dict)
cursor.close()
conn.close()
