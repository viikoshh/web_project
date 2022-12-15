from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from blog.models import Comment, Post
from blog.serializers import CommentSerializer, BlogPostListSerializer, BlogPostDetailSerializer, \
    BlogPostCreateUpdateSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    A viewsets for viewing and editing user instances in
    django_progect project.
    """
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class ActionSerializedViewSet(viewsets.ModelViewSet):
    action_serializer = {}

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            if self.action in self.action_serializers:
                return self.action_serializers[self.action]

        return self.serializer_class


class BlogPostViewSet(ActionSerializedViewSet):
    serializer_class = BlogPostListSerializer
    queryset = Post.objects.all()

    action_serializers = {
        'list': BlogPostListSerializer,
        'retrieve': BlogPostDetailSerializer,
        'create': BlogPostCreateUpdateSerializer,
        'update': BlogPostCreateUpdateSerializer,
    }

    def get_queryset(self):
        queryset = self.queryset
        author = self.request.query_params.get('author', None)
        if author:
            queryset = queryset.filter(author_username=author)
        return queryset

    @action(detail=False)
    def published_posts(self, request):
        published_posts = Post.published.all()
        page = self.paginate_queryset(published_posts)
        if page is not None:
            serializers = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializers.data)

        serializer = self.get_serializer(published_posts, many=True)
        return Response(serializer.data)

    @action(detail=True,
            methods=['post'],
            permission_classes=[IsAuthenticated])
    def publish(self, request, pk=None):
        post = self.get_object()
        if request.user == post.author:
            return Response({'message': 'blog post was published'},
                            status=status.HTTP_200_OK)
        else:
            return Response({'message': 'You don\t have permission'},
                            status=status.HTTP_403_FORBIDDEN)

