from django.urls import path
from . import views


app_name = 'baseApp'

urlpatterns = [
    path('', views.home_view, name="home"),
    path('about/', views.about_view, name="about"),
    path('abstract/', views.abstract_view, name="abstract"),
]