from django.db import models

from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=32,verbose_name="用户名")
    pwd=models.CharField(max_length=32,verbose_name="密码")
    roles=models.ManyToManyField(to="Role",verbose_name="角色")

    def __str__(self): return self.name

    class Meta:
        verbose_name="用户表"
        verbose_name_plural=verbose_name
class Role(models.Model):
    title=models.CharField(max_length=32,verbose_name="角色")
    permissions=models.ManyToManyField(to="Permission",verbose_name="权限")

    def __str__(self): return self.title

    class Meta:
        verbose_name="角色表"
        verbose_name_plural=verbose_name

class Permission(models.Model):
    title=models.CharField(max_length=32,verbose_name="权限")
    url=models.CharField(max_length=32,verbose_name="路径")
    action= models.CharField(max_length=32,default="",verbose_name="操作描述")
    # 目的是为了方便布局,判断有没有增删改操作

    permissions_group=models.ForeignKey(to="Permissions_group",verbose_name="分组",on_delete=models.CASCADE,default=1)

    def __str__(self):return self.title

    class Meta:
        verbose_name = "权限管理"
        verbose_name_plural = verbose_name



 # 目的是区分对那张表操作,方便布局命名
class Permissions_group(models.Model):
    role_group=models.CharField(max_length=32,verbose_name="角色")

    def __str__(self): return self.role_group

    class Meta:
        verbose_name = "分组"
        verbose_name_plural = verbose_name