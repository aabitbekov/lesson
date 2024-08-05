from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']

class PostTitleFilterForm(forms.Form):
    title = forms.CharField(max_length=200, label='search into title')
