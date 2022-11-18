from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('posts/<int:id>/edit', views.post_edit, name='post_edit'),
    path('posts/add/', views.post_edit, name='post_add'),
]