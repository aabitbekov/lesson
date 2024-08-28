
from django.forms import model_to_dict
from mainapp.models import Author, Post
from .serializers import AuthorSerializer, PostSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, mixins, generics, filters
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from .paginator import AuthorPaginator
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# class AuthorListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer


# class AuthorDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer


class AuthorAPIViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'email']
    search_fields = ['name', 'email']
    pagination_class = AuthorPaginator

    @action(methods=['get'], detail=True)
    def names(self, request, pk=None):
        author = Author.objects.get(pk=pk)
        return Response({'author' : model_to_dict(author)})
            

class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class PostDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


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
    
