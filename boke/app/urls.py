from django.conf.urls import url

from . import views

urlpatterns = [
    # 列表
    url(r'^list_boke/$',views.list_boke,name='list_boke'),
    # 编辑
    url(r'^edit_boke/$', views.edit_boke, name='edit_boke'),
    # 阅读
    url(r'^read_boke/$', views.read_boke, name='read_boke'),
    # 创建
    url(r'^create_boke/$', views.create_boke, name='create_boke'),
    # 搜索
    url(r'^search_boke/$', views.search_boke, name='search_boke'),


]