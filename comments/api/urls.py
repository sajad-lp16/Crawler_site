from django.urls import path

from . import views

app_name = 'comments-api'

urlpatterns = [
    path('list-create/', views.CommentListCreateAPI.as_view(), name='comment_list_create'),

    path('ret-up-dest/<int:pk>/',
         views.CommentRetrieveUpdateDestroyAPI.as_view(), name='comment_retrieve_update_destroy'),
]
