from django.db import models


class UserInfo(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    age = models.IntegerField()


# 自动生成id列 bigint 自增，primarykey
#不想要什么内容（表，行）直接注释再重新执行即可
