#!/usr/bin/env python
# -*- coding:utf-8 -*-



# by luffycity.com
import re
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import  HttpResponse,redirect,reverse

# 校验是否有访问权限
def reg(request,current_path):
    # 校验权限1(permission_list)
    permission_list = request.session.get("user_url", [])

    """
    /user/add       # 前台没加后面的下划线,匹配不上
    
    ['/role/', '/user/', '/user/update/', '/user/add/', '/user/delete/']
    """

    flag = False
    for permission in permission_list:

        permission = "^%s$" % permission

        ret = re.match(permission, current_path)
        if ret:
            flag = True
            break
    return flag





class ValidPermission(MiddlewareMixin):

    def process_request(self,request):


        # 当前访问路径
        current_path = request.path_info



        # 检查是否属于白名单
        valid_url_list=["/reg/","/admin/.*","/login/",'/get_code/','/check_code/',"/home/"]



        for valid_url in valid_url_list:
            ret=re.match(valid_url,current_path)
            if ret:
                return None


        # 校验是否登录
        user_id=request.session.get("user_pk","")

        if not user_id:
            url=reverse("login")
            return redirect(url+"?url=%s"%current_path)


        # #校验权限1(permission_list)
        # # permission_list = request.session.get("user_url",[])  # ['/users/', '/users/add', '/users/delete/(\\d+)', 'users/edit/(\\d+)']
        # flag=reg(request,current_path)
        #
        # if not flag:
        #     return HttpResponse("没有访问权限！")
        #
        # return None

        ##校验权限2

        permission_dict=request.session.get("permission_dict")

        for item in permission_dict.values():
              urls=item['urls']
              for reg in urls:
                  reg="^%s$"%reg
                  ret=re.match(reg,current_path)
                  if ret:
                      request.actions=item['actions']
                            #   在视图函数中知道其有什么操作权限
                      # request.urls1=item['urls']
                            # 因为已经匹配上自己需要访问的表路径,就不需要添加其他权限路径了
                      return None

        return HttpResponse("没有访问权限！")
