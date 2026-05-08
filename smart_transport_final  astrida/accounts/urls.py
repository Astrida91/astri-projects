from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView
app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),

    path('accounts/profile/', views.profile_view, name='profile'),

    path('profile/edit/', views.profile_edit_view, name='profile_edit'),

    path('change-password/', views.change_password, name='change_password'),
    path('change-password/', PasswordChangeView.as_view(), name='change_password')


]
