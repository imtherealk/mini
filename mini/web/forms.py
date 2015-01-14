from django import forms
from django.contrib.auth.models import User
from mini.web.models import UserProfile, Post, Comment
__author__ = 'my'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),
                               error_messages={'required': '비밀번호를 입력해주세요'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        help_texts = {
            'username': '(알파벳, 숫자, @/./+/-/_만 가능)'
        }
        error_messages = {
            'username': {
                'required': '사용자명을 입력해주세요',
            },
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('relationship_status', 'profile_image')
