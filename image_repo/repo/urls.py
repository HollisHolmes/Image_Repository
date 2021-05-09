from django.urls import path
from . import views

app_name = 'repo'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('<str:name>', views.main, name='main'),
]
