from django.urls import path, re_path
from core import views


urlpatterns = [
    path('register/', views.register, name=('register')),
    path('login/', views.login_view, name=('login')),
    path('logout/', views.logout_view, name=('logout')),
    path('Dashboard/', views.Dashboard, name=('dashboard')),
]

