from django.shortcuts import render, redirect
from app01 import models


def depart_list(request):
    """部门信息"""
    queryset = models.Department.objects.all()

    return render(request, "depart_list.html", {'queryset': queryset})


def depart_add(request):
    """添加部门"""
    if request.method == "GET":
        return render(request, "depart_add.html")

    title = request.POST.get("title")
    models.Department.objects.create(title=title)
    return redirect("/depart/list/")


def depart_delete(request):
    """删除部门"""
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()
    return redirect("/depart/list/")


def depart_edit(request, nid):
    """编辑部门"""
    if request.method == "GET":
        row_object = models.Department.objects.filter(id=nid).first()

        # print(row_object.id, row_object.title)  # 只是放在了后台
        return render(request, 'depart_edit.html', {"row_object": row_object})
    else:
        title = request.POST.get("title")
        print(request.POST.get("title"))
        models.Department.objects.filter(id=nid).update(title=title)
        return redirect("/depart/list/")


# 目前进行到还是add替换的edit，非独立
# 用户表
def user_list(request):
    queryset = models.UserInfo.objects.all()
    # 下述是用python语法获取数据方式：
    """for obj in queryset:
        print(obj.id, obj.name, obj.account, obj.create_time.strftime("%Y-%m-%d"), obj.gender, obj.get_gender_display(),
              obj.depart_id, obj.depart.title)
    """
    return render(request, 'user_list.html', {"queryset": queryset})


def user_add(request):
    """添加用户(原始方式)"""
    if request.method == "GET":
        context = {
            'gender_choices': models.UserInfo.gender_choices,
            'depart_list': models.Department.objects.all()
        }
        return render(request, 'user_add.html', context)
    # 获取用户输入数据(传统本质方法）
    name = request.POST.get("name")
    password = request.POST.get("password")
    age = request.POST.get("age")
    account = request.POST.get("account")
    create_time = request.POST.get("create_time")
    gender = request.POST.get("gender")
    depart = request.POST.get("depart")
    models.UserInfo.objects.create(name=name, password=password, age=age, account=account, create_time=create_time,
                                   gender=gender, depart_id=depart)
    return redirect("/user/list/")