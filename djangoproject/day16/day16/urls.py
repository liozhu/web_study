from django.contrib import admin
from django.urls import path
from app01 import views

urlpatterns = [
    # 部门表
    path('depart/list/', views.depart_list),
    path('depart/add/', views.depart_add),
    path('depart/delete/', views.depart_delete),
    # 必须中间带有数据:http://127.0.0.1:8000/depart/10/list/
    path('depart/<int:nid>/edit/', views.depart_edit),

    # 用户表
    path('user/list/', views.user_list),
    path('user/add/', views.user_add),
]
