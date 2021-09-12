from django.urls import path, include

from . import views

app_name = 'accounts'

urlpatterns = [
    path('api/', include('accounts.api.urls', namespace='accounts_api')),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.LogOutUser.as_view(), name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('profile/', views.UserProfile.as_view(), name='profile'),
    path('edit-profile/', views.EditProfile.as_view(), name='edit_profile'),
    path('reset/', views.PasswordReset.as_view(), name='password_reset'),
    path('reset/done/', views.PasswordResetDone.as_view(), name='password_reset_done'),
    path('reset/confirm/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('reset/complete/', views.PasswordResetComplete.as_view(), name='password_reset_complete'),

]
