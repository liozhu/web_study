from flask import Flask, render_template, request
import pymysql

app=Flask(__name__)
@app.route("/add/user", methods=["GET", "POST"])
def add_user():
    if request.method == "GET":
        return render_template("add_user.html")
    else:
        username = request.form.get("user")
        password = request.form.get("pwd")
        mobile = request.form.get("mobile")

        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="zjl195834", charset="utf8",
                               db="pymysql")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        sql = "insert into admin(username,passwd,mobile) values (%s,%s,%s)"
        cursor.execute(sql, [username, password, mobile])
        conn.commit()

        cursor.close()
        conn.close()
        return "添加成功"


@app.route("/show/user",methods=["GET","POST"])
def show_user():
    username=request.form.get('user')
    password = request.form.get("pwd")
    mobile = request.form.get("mobile")

    conn=pymysql.connect(host="127.0.0.1",port=3306,user="root",password="zjl195834",charset='utf8',db='pymysql')
    cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)

    sql="select * from admin"
    cursor.execute(sql)
    data_list=cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("show_user.html",data_list=data_list)

if __name__ == '__main__':
    app.run()
