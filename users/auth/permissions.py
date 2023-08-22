from rest_framework.permissions import BasePermission

class IsAuthenticated(BasePermission):
    """
    Allows access only to authenticated devices.
    """

    def has_permission(self, request, view):
        try:
            print("Authorization => ", request.META.get('HTTP_AUTHORIZATION', b''))
            print("Requested User", request.user)
            return request.user
        except:
            return False