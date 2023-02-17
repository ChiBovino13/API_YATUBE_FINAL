from rest_framework import filters, mixins, permissions, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.permissions import IsAuthorOrReadOnlyPermission
from api.serializers import (CommentSerializer, FollowSerializer,
                             GroupSerializer, PostSerializer)
from posts.models import Group, Post


class PostViewSet(viewsets.ModelViewSet):
    """Описание операций, выполняемых с публикациями."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnlyPermission
    )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Описание операций, выполняемых с комментариями."""
    serializer_class = CommentSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnlyPermission,
    )

    def perform_create(self, serializer):
        post = get_object_or_404(
            Post,
            id=self.kwargs.get('post_id')
        )
        serializer.save(
            author=self.request.user,
            post=post
        )

    def get_queryset(self):
        return get_object_or_404(
            Post,
            id=self.kwargs.get('post_id')
        ).comments


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Описание операций, выполняемых с группами."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FollowViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """Описание операций, выполняемых с подписками."""
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['following__username']

    def get_queryset(self):
        return self.request.user.follower

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
