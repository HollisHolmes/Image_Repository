from django.urls import path
from . import views

app_name = 'repo'
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('myitems', views.myitems, name='myitems'),
]
