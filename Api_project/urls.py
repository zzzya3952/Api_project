"""Api_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Api_app.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('help', v_help),
    path('', login),
    path('accounts/login/', login),  # 没有登录，通过url进来的
    path('login_action/', login_action),
    path('register_action/', register_action),
    # path('index/', TemplateView.as_view(template_name='index.html')),
    path('index/', index),
    path('get_tj_datas/', get_tj_datas),
    path('get_real_time_datas/', get_real_time_datas),
    path('logout/', logout),
    path('get_project_list/', get_project_list),
    path('add_project/', add_project),
    path('delete_project/', delete_project),
    path('get_project_detail/', get_project_detail),
    path('save_project/', save_project),
]
