from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsAuthorOrReadOnlyPermission(permissions.BasePermission):
    """Разарешение только безопасные методы, если не автор поста."""

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.method in SAFE_METHODS
