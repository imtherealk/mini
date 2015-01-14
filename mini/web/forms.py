from django import forms
from django.contrib.auth.models import User
from mini.web.models import UserProfile, Post, Comment
__author__ = 'my'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('relationship_status', 'profile_image')
