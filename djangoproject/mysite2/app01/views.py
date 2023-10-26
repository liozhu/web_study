from wsgiref import headers

from django.shortcuts import render, HttpResponse, redirect
from app01.models import UserInfo


# Create your views here.

def index(request):
    return HttpResponse("欢迎使用")


def user_list(request):
    return render(request, "user_list.html")


def news(request):
    # http://www.chinaunicom.com/api/article/NewsByIndex/2/2023/10/news

    import requests
    res = requests.get("http://www.chinaunicom.com/api/article/NewsByIndex/2/2023/10/news", headers)
    data_list = res.json()
    print(data_list)

    return render(request, 'news.html', {"news_list": data_list})


def something(request):
    return redirect("https://www.baidu.com")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        print(request.POST)
        username = request.POST.get("user")
        password = request.POST.get("pwd")
        if username == 'root' and password == '123':
            return redirect("http://www.chinaunicom.com/")
        else:
            return render(request, 'login.html', {"error_msg": "用户名或密码错误"})


def info_user(request):
    data_list = UserInfo.objects.all()
    return render(request, 'info_user.html', {"data_list": data_list})


def info_add(request):
    if request.method == 'GET':
        return render(request, 'info_add.html')
    else:
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        age = request.POST.get("age")
        UserInfo.objects.create(name=user, password=pwd, age=age)
        return redirect("/info/user/")


def info_delete(request):
    nid = request.GET.get('nid')
    UserInfo.objects.filter(id=nid).delete()
    return redirect('/info/user/')
