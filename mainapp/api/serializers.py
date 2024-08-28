
from mainapp.models import Author, Post
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = []

class AuthorSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = ['id', 'name']

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer2()

    class Meta:
        model = Post
        exclude = []
        fields = ['author', 'title', 'content', 'created_at']

