from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post
from .serializers import PostsSerializer


class PostsAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()

        return Response({'Posts': PostsSerializer(posts, many=True).data})

    def post(self, request):
        serializer = PostsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        new_post = Post.objects.create(
            title=request.data['title'],
            text=request.data['text'],
        )

        return Response({'Post': PostsSerializer(new_post).data})

    def put(self):
        pass
