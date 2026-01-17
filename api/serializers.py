from django.contrib.auth.models import Group, User
from rest_framework import serializers
from newspaper.models import Tag

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "groups", "first_name", "last_name", "date_joined"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name"]

class TagSerializer(serializers.ModelSerializer):
     class Meta:
         model = Tag
         fields = ["id", "name"]

