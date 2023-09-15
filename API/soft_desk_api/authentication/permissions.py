from rest_framework.permissions import BasePermission
from authentication.models import User

class IsUser(BasePermission):
    

    def has_permission(self, request, view):
        if view.action == "list":
            return bool(request.user and request.user.is_authenticated)
        
        if view.action == "retrieve":
            return bool(request.user and request.user.is_authenticated)
        
        if view.action == "update" or view.action == "partial_update" or view.action == "destroy":
            self.message = "You can update or delete only your account"
            user_id = int(view.kwargs.get('pk'))

            return bool(request.user and request.user.is_authenticated and user_id == request.user.id)
    
        return bool(request.user and request.user.is_authenticated)