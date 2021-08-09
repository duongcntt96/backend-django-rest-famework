from django.contrib.auth.models import User, Group
from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.HyperlinkedModelSerializer):
    field_name_map = {
        'id': 'pk'
    }
    class Meta:
        model = Post
        fields = ['id','title', 'body', 'created']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']