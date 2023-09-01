from rest_framework import serializers

from .models import Post


class PostsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    text = serializers.CharField()
    date_of_post = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
