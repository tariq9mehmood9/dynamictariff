from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('logout', views.logout_view, name='logout'),
    path('activate/<uidb64>/<token>', views.ActivateView, name='activate'),
    # path('set-new-password/<uidb64>/<token>', views.SetNewPasswordView.as_view(), name='set-new-password'),
]