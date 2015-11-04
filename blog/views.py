from django.shortcuts import render, render_to_response
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from blog.serializers import PostSerializer
from models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def create(self, request, *args, **kwargs):
        data = request.data
        data['user'] = request.user.pk

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            Post.objects.create(
                title=serializer.validated_data['title'],
                description=serializer.validated_data['description'],
                user=serializer.validated_data['user']
            )
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=500)

