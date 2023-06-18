from rest_framework import serializers

from .models import Posts


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'author',
            'body',
        )
        model = Posts
