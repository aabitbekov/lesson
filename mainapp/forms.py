import datetime
from django.forms import ModelForm, Textarea
from django import forms
from .models import Author, Post
from django.utils.translation import gettext_lazy as _

class SimpleForm(forms.Form):
    day = forms.DateField(initial=datetime.date.today)
    name = forms.CharField(max_length=128, label='Your name')
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea)
    cc_myself = forms.BooleanField(required=False)


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'