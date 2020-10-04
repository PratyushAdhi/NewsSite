from rest_framework import permissions

class IsAuthorOrModeratorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if obj.author == request.user:
                return True
            elif request.user.is_moderator or request.user.is_admin:
                return True
            else:
                return False

