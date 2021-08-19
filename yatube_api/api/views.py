# TODO:  Напишите свой вариант
from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from posts.models import Comment, Follow, Group, Post

from .permissions import IsAuthorOrReadOnlyPermission
from .serializers import (CommentSerializer, FollowSerializers,
                          GroupSerializer, PostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission, IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission, IsAuthenticated)

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(post=post, author=self.request.user)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializers
    permission_classes = (IsAuthorOrReadOnlyPermission, IsAuthenticated)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['=user__username', '=following__username']
