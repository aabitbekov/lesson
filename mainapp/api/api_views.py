
from django.forms import model_to_dict
from mainapp.models import Author, Post
from rest_framework import generics
from .serializers import AuthorSerializer, PostSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class AuthorListAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CustomAPIView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        return Response({'authors' : AuthorSerializer(authors, many=True).data})

    def post(self, request):
        author = Author.objects.create(
            name=request.data['fullname'],
            email=request.data['email']
        )
        return Response({'author': model_to_dict(author)})