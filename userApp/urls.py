from django.urls import path
from . import views

app_name = 'userApp'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('profile/', views.profile_view, name='profile'),
    path('test/', views.test_view, name='test')
]