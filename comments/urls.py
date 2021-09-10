from django.urls import path, include

from . import views

app_name = 'comments'

urlpatterns = [
    path('api/', include('comments.api.urls',namespace='comments-api')),
    path('list/', views.CommentList.as_view(), name='comment_list'),
    path('detail/<int:pk>/', views.CommentDetailView.as_view(), name='comment_detail'),
    path('create/<int:pk>/', views.CommentCreate.as_view(), name='comment_create'),
    path('update/<int:pk>/', views.CommentUpdate.as_view(), name='comment_update'),
    path('delete/<int:pk>/', views.CommentDeleteView.as_view(), name='comment_delete'),

]
