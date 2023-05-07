from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    only authenticated user add, only owner can delete/put, AnyOne can read
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.party.user == request.user


class IsOwnerOrAuthenticated(permissions.BasePermission):
    """
    only authenticated user can add/read, only owner can delete/put,
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.party.user == request.user


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    only staff users can add/delete/put, AnyOne can read
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff


class IsAdminOrAuthenticated(permissions.BasePermission):
    """
    only staff users can add/delete/put, Authenticated user can read
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated
        return request.user.is_staff
