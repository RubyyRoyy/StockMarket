from django.urls import path
from users.views import register,profile
from django.contrib.auth import views

urlpatterns = [
    path('register/', register, name="register"),
    path('profile/', profile, name="profile"),
    path('', views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
]
