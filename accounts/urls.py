from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.LogOutUser.as_view(), name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('profile/', views.UserProfile.as_view(), name='profile'),
    path('edit-profile/', views.EditProfile.as_view(), name='edit_profile'),
]
