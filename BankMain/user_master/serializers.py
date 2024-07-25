from djoser.serializers import UserCreateSerializer , UserSerializer
from rest_framework import serializers
from .models import UserAccount, UserAccountManager

class CustomUserCreateSerializer(UserCreateSerializer):
    role = serializers.ChoiceField(choices=UserAccount.Roles)

    class Meta:
        model = UserAccount
        fields = ('email', 'password', 'name', 'role')  # Include 'role'

    def create(self, validated_data):
        role = validated_data.pop('role')
        user = UserAccountManager.create_user(**validated_data)
        user.role = role
        user.save()
        return user
    
class UserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = UserAccount
        fields = ('id', 'name', 'email', 'role')

class UserStatus(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = UserAccount
        fields = ['is_active']