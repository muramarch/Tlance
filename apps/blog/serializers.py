from rest_framework import serializers

from .models import Post, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = {
            'id',
            'name',
        }


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content',
            'pvd_date',
            'update_date',
            'delet_date',
            'author',
            'tags',
        )