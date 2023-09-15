from rest_framework.serializers import ModelSerializer, CharField
from authentication.models import User


class UserListSerializer(ModelSerializer):
    password = CharField(write_only="True")

    class Meta:
        model = User
        fields = ['id', 'username', 'age', 'can_be_contacted', 'can_data_be_shared', 'created_time', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
