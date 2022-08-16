from django.shortcuts import render
from Api_app.models import *
# Create your views here.
import time
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import logging
import json


def v_help(request):
    return render(request, 'help.html')


# 进入登录页的函数
def login(request, message=''):
    res = {}
    res["notices"] = list(DB_notice.objects.all().values('content'))[::-1][:2]  # 倒序与切片
    res["message"] = message

    return render(request, 'login.html', res)


# 登录功能
def login_action(request):
    time.sleep(1)

    # 获取用户名/密码
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)

    # 去数据库进行比对
    user = auth.authenticate(username=username, password=password)
    if user is None:  # 用户名/密码错误
        return login(request)
    else:  # 代表验证成功
        # 登录
        auth.login(request, user)
        request.session['user'] = username
        # 跳转到首页
        return HttpResponseRedirect('/index/')


# 注册功能
def register_action(request):
    time.sleep(1)

    # 获取用户名/密码
    username = request.GET['username']
    password = request.GET['password']
    print(username, password)

    # 去数据库注册
    try:  # 注册成功
        user = User.objects.create_user(username=username, password=password)
        user.save()

        # 登录
        auth.login(request, user)
        request.session['user'] = username

        # 跳转到首页
        return HttpResponseRedirect('/index/')
    except:  # 用户已存在
        return login(request, '用户名')


# 退出功能
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


@login_required()
def index(request):
    return render(request, 'index.html')


# 获取统计函数
def get_tj_datas(request):
    # 获取用户id
    userID = request.user.id

    tj_datas = {}
    tj_datas["notices"] = list(DB_notice.objects.all().values('content'))[::-1]
    tj_datas["news"] = list(DB_news.objects.filter(to_user_id=userID).values())[::-1]
    for i in tj_datas["news"]:
        from_user_name = get_object_or_404(User, pk=i["from_user_id"]).username
        i["from_user_name"] = from_user_name
        i["content"] = i["content"][:10] + '...' if len(i['content']) > 10 else i['content']

    tj_datas["overview"] = {
        "project_count": 120,
        "case_count": 130,
        "api_count": 140,
        "env_count": 150,
        "user_count": 160,
    }
    tj_datas["monitor"] = {
        "case_pass": 80,
        "api_pass": 99,
        "case_fail": 20
    }
    tj_datas["contribution"] = {
        "project": 50,
        "case": 22,
        "api": 74,
        "monitor": 38,
    }
    return HttpResponse(json.dumps(tj_datas), content_type='application/json')


# 获取实时数据
def get_real_time_datas(request):
    real_time_daras = {
        "ApiShop_count": 66,
        "UnRendNews_counts": 77,
        "RunCase_count": 88,
        "Import_count": 99, }
    return HttpResponse(json.dumps(real_time_daras), content_type='application/json')


# 获取项目列表数据
def get_project_list(request):
    keys = request.GET.get('keys', None)
    if keys:
        project_list_data = list((DB_project_list.objects.filter(name__contains=keys,
                                                                 deleted=False) | DB_project_list.objects.filter(
            des__contains=keys, deleted=False)).values())[
                            ::-1]  # select * from 表 where name like %keys% or des like %keys% ;
    else:
        project_list_data = list(DB_project_list.objects.all().values())[::-1]

    # 增加字段 creater_name
    for i in project_list_data:
        try:
            creater_name = get_object_or_404(User, pk=i['creater']).username
        except:
            creater_name = '无人认领'
        i["creater_name"] = creater_name
    return HttpResponse(json.dumps(project_list_data), content_type='application/json')


# 增加项目
def add_project(request):
    uid = request.user.id if request.user.id else 0
    DB_project_list.objects.create(creater=uid)
    return get_project_list(request)


# 删除项目
def delete_project(request):
    project_id = request.GET['project_id']
    DB_project_list.objects.filter(id=project_id).delete()
    return get_project_list(request)


# 获取单个项目详情
def get_project_detail(request):
    id = request.GET['id']
    form = list(DB_project_list.objects.filter(id=id).values())[0]
    return HttpResponse(json.dumps(form), content_type='application/json')


# 保存项目
def save_project(request):
    form = json.loads(request.body.decode('utf-8'))
    DB_project_list.objects.filter(id=form['id']).update(**form)
    return HttpResponse('', content_type='application/json')
