
from mainapp.models import Author, Post
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = ['email',]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = []

