from django import forms
from django.contrib.auth.models import User

from .models import Publisher, Author


class PublisherForm(forms.ModelForm):

    class Meta:
        model = Publisher
        fields = ['publisher_name', 'publisher_link', 'publisher_logo']


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['author_name', 'author_image', 'author_slug']


"""
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        """
