from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, PasswordChangeDoneView, PasswordChangeView, logout_then_login, LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('login/', views.user_login, name='login')

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout-then-login/', logout_then_login, name='logout_then_login'),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('', views.dashboard, name='dashboard')

    ]