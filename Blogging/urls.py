from django.urls import path
from . import views
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

app_name = 'Blogging'
urlpatterns = [
    path('', views.blog_home, name='BlogHome'),
    path('user_index/', views.UserIndexView.as_view(), name='user_index'),
    path('create_user/', views.signup, name='create_user'),
    path('<int:pk>/', views.ProfileView.as_view(), name='profile_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='Blogging/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Blogging/logout.html'), name='logout'),
    path('<int:pk>/profile_edit', views.EditProfileView, name='profile_edit'),
]

