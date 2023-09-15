from rest_framework.permissions import BasePermission


class IsOwnerOrAdminOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return request.user.is_authenticated
        return request.user.is_authenticated and request.user == obj.owner or request.user.is_staff