from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/register",methods=['GET'])
def register():
    return render_template("register.html")

@app.route("/do/reg" , methods=['GET'])
def do_register():
    print(request.args)
    return "注册成功"


@app.route("/post/reg" , methods=['POST'])
def post_register():
    print(request.form)
    return "注册成功"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5200,debug=False)


