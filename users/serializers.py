from dataclasses import fields
from rest_framework import serializers

from .models import Profile
from .User import User

class UserSerializer(serializers.ModelSerializer):
    # profile = serializers.PrimaryKeyRelatedField(many=True, queryset=Profile.objects.all())
    class Meta:
        model = User
        fields = ['email', 'password', 'profile']


class ProfileSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone', 'user']