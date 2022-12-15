from rest_framework import serializers

from blog.models import Comment, Post
from django import forms


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'created_date', 'text', 'approve')


class BlogPostListSerializer(serializers.ModelSerializer):
    preview_text = serializers.SerializerMethodField()

    def get_preview_text(self, post):
        return post.get_text_preview()

    class Meta:
        model = Post
        fields = ('title', 'author', 'created_date', 'preview_text')


class BlogPostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ()


class BlogPostDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.SerializerMethodField()

    def get_comments_count(self, obj):
        return obj.comments_count()

    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'published_date',
                  'comments_count')