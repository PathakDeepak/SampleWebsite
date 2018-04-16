

from django.urls import path
from django.conf.urls import url

from accounts import views

urlpatterns = [
    path(r'login/',views.login),
    path(r'/',views.logout),
   #url(r'^home',views.logout),
]  