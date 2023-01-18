from rest_framework import permissions
from chat.models import Participate

# only owner can delete/put, only participated user can read
class MessagePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return Participate.objects.filter(room__id=view.kwargs['room'],
                                                 party=request.user.party)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.party.user == request.user

