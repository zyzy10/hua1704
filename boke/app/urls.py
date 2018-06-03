from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list_boke/$',views.list_boke,name='list_boke'),
]