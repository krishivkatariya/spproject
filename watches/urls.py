from django.urls import path
from . import views

app_name = 'watches'

urlpatterns = [
    path('', views.watch_list, name='watch_list'),
    path('add/', views.add_watch, name='watch_add'),
    path('watch/<int:pk>/', views.watch_detail, name='watch_detail'),
]
