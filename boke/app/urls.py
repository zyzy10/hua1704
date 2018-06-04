from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list_boke/$',views.List_boke.as_view(),name='list_boke'),
    url(r'^search_boke/$', views.Search_boke.as_view(), name='search_boke'),
    url(r'^cseate_boke/$', views.Cseate_boke.as_view(), name='cseate_boke'),
    url(r'^update_boke/$', views.update_boke.as_view(), name='update_boke'),
    url(r'^up_post/(?P<tid>\d+)/$',views.up_post,name='up_post'),
    # url(r'^detail_boke/(?P<tid>\d+)/$', views.Detail_boke.as_view(), name='detail_boke'),
    url(r'^detail_boke/$', views.Detail_boke.as_view(), name='detail_boke'),

]