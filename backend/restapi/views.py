from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from api.models import Post
from .serializers import PostSerializer
from rest_framework import generics

class ListUsers(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)

class GetListPosts(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        post = Post.objects.all()
        data = PostSerializer(post,many=True)
        # return HttpResponse(str(post.id)+ "<br>" + post.title + "<br>" + post.body)
        
        return Response(data=data.data,status=status.HTTP_200_OK)
class SearchPost(generics.ListAPIView):
    serializer_class = PostSerializer
    def get_queryset(self):
        q = self.kwargs['q']
        return Post.objects.filter(title__contains=q)