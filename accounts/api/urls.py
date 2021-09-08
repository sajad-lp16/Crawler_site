from django.urls import path

from . import views

app_name = 'accounts_api'

urlpatterns = [
    path('list-create/', views.UserListCreateAPI.as_view(), name='list_create'),
    path('ret-up-dest/<str:username>/', views.UserRetrieveUpdateDestroy.as_view(), name='retrieve_update_destroy'),
]
