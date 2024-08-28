from django.urls import path, include
from .views import *
from mainapp.api.api_views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'author', AuthorAPIViewSet)

app_name = 'mainapp'

urlpatterns = [
    path('api/v3/', include(router.urls)),
    # path('api/v3/authors/', AuthorAPIViewSet.as_view({'get' : 'list'})),
    # path('api/v3/authors/create/', AuthorAPIViewSet.as_view({'post' : 'create'})),
    # path('api/v3/author/detail/<int:pk>/', AuthorAPIViewSet.as_view({'get' : 'retrieve'})),
    # path('api/v3/author/update/<int:pk>/', AuthorAPIViewSet.as_view({'put' : 'update'})),
    # path('api/v3/author/delete/<int:pk>/', AuthorAPIViewSet.as_view({'delete' : 'destroy'})),



    # path('api/v2/authors/', AuthorListCreateAPIView.as_view()),
    # path('api/v2/author/<int:pk>/', AuthorDetailUpdateDeleteAPIView.as_view()),

    path('api/v2/posts/', PostListCreateAPIView.as_view()),
    path('api/v2/post/<int:pk>/', PostDetailUpdateDeleteAPIView.as_view()),

    # path('', PostListView.as_view(), name='post-list'),
    # path('post/<int:pk>/', PostDetailListView.as_view(), name='post-detail'),

    # path('post/', new_page, name='second'),
    # path('post/delete/', new_page, name='second'),
    # path('redirect/', redirect_to_index, name='test'),
    
    # path('send_form/', my_form, name='send_form'),
    # path('author_form/', author_form, name='author_form'),
    # path('author_form/edit/<int:author_id>/', author_edit_form, name='author_edit_form'),
]


