from django.urls import path, include
from rest_framework import routers

from core.views import CommentViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'comments', CommentViewSet)

urlpatterns = [
    #path('', views.post_list, name='post_list'),
    path('', include(router.urls)),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('posts/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('posts/<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('posts/add/', views.post_edit, name='post_add'),
]