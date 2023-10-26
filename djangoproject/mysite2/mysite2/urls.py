from django.contrib import admin
from django.urls import path
from app01 import views

urlpatterns = [
    #
    path('index/',views.index),

    path('user/list/',views.user_list),

    path('news/',views.news),

    path('something/',views.something),

    path('login/',views.login),

    path('info/user/',views.info_user),
    path('info/add/',views.info_add),
    path('info/delete/',views.info_delete)
]
