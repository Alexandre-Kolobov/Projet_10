from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.viewsets import ModelViewSet
from authentication.models import User
from authentication.serializers import UserListSerializer
from authentication.permissions import IsUser

class UserViewset(ModelViewSet):
    serializer_class = UserListSerializer
    permission_classes = [IsUser]
        
    def get_queryset(self):
        queryset = User.objects.all()
        return queryset