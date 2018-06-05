from django.conf.urls import url

from . import views

urlpatterns = [
    # 登录
    url(r'^login/$',views.login,name='login'),
    # 注册
    url(r'^register/$', views.register, name='register'),
    # 阅读
    url(r'^user_info/$', views.user_info, name='user_info'),
    # 退出
    url(r'^logout/',views.logout,name='logout'),


]