import django_filters
from .models import Post
from django import forms

class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='contains',
        label='Название:'
    )
    created_at__gte = django_filters.DateTimeFilter(
        field_name='created_at',
        lookup_expr='gte',
        label='C какого:',
        widget=forms.DateTimeInput(attrs={'type' : 'date'})
    )
    created_at__lte = django_filters.DateTimeFilter(
        field_name='created_at',
        lookup_expr='lte',
        label='По какое:',
        widget=forms.DateTimeInput(attrs={'type' : 'date'})
    )
    custom_field = django_filters.CharFilter(
        label="Search",
        method='custom_filter'
    )
    author_username = django_filters.CharFilter(
        field_name='author__username',
        lookup_expr='contains'
    )
    class Meta:
        model = Post
        # fields = ['title', 'content']
        # fields = {
        #     'title' : ['contains'],
        #     'content' : ['contains'],
        #     'created_at' : ['lte', 'gte']
        # }
        fields = []
    
    def custom_filter(self, queryset, name, value):
        # logic
        return queryset.filter(author__username__contains=value)

