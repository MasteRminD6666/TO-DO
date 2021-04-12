from django.conf.urls import url
from Home import views
from django.urls import include, path

urlpatterns = [
    path('',  views.home ,name='index'),

]
