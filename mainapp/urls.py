from django.urls import path
from .views import *
from mainapp.api.api_views import AuthorListAPIView, CustomAPIView, PostListAPIView

app_name = 'mainapp'

urlpatterns = [
    path('api/v1/authors/', AuthorListAPIView.as_view()),
    path('api/v1/customview/', CustomAPIView.as_view()),
    path('api/v1/posts/', PostListAPIView.as_view()),
    # path('', PostListView.as_view(), name='post-list'),
    # path('post/<int:pk>/', PostDetailListView.as_view(), name='post-detail'),


    # path('post/', new_page, name='second'),
    # path('post/delete/', new_page, name='second'),
    # path('redirect/', redirect_to_index, name='test'),
    
    # path('send_form/', my_form, name='send_form'),
    # path('author_form/', author_form, name='author_form'),
    # path('author_form/edit/<int:author_id>/', author_edit_form, name='author_edit_form'),


]


