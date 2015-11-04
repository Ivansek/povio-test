from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from blog.models import Post

class UserSerializer(serializers.Serializer):
    """
    Serializer for Django User model
    """
    username = serializers.CharField(max_length=50)

    # class Meta:
    #     model = User
    #     fields = ('id', 'username', 'email', 'first_name')
    #     read_only_fields = ('__all__')

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'featured', 'user')
        # read_only_fields = ('user')

    def create(self, validated_data):
        p = Post.objects.create(title=validated_data['title'],
                                description=validated_data['description'],
                                user=User.objects.get(username=validated_data['user']['username'])
        )
        return p
    #
    # def to_internal_value(self, data):
    #     data['user'] = UserSerializer(data['user']).data
    #     return data