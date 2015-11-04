from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from blog.serializers import PostSerializer, UserSerializer
from models import Post


class PostViewSet(viewsets.ModelViewSet):
    """
    ViewSet for blog post
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def create(self, request, *args, **kwargs):
        """
        Override create method in order to add user in serializer
        """
        data = request.data
        data['user'] = UserSerializer(request.user).data
        return super(self.__class__, self).create(request, args, kwargs)