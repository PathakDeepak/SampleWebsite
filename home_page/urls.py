from django.urls import path
from django.conf.urls import url

from home_page import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]
