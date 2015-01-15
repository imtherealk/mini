from django import forms
from django.contrib.auth.models import User
from mini.web.models import UserProfile, Post, Comment
__author__ = 'my'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),
                               error_messages={'required': '비밀번호를 입력해주세요'},
                               help_text='*',
                               label='비밀번호')

    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        help_texts = {
            'username': '* (알파벳, 숫자, @/./+/-/_)',
        }
        error_messages = {
            'username': {
                'required': '사용자명을 입력해주세요',
            },
        }


class UserProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['birth'].label = '생일'
        self.fields['relationship_status'].label = '상태'
        self.fields['profile_image'].label = '프로필 사진'

    class Meta:
        model = UserProfile
        fields = ('birth', 'relationship_status', 'profile_image')
        help_texts = {
            'birth': '(yyyy-mm-dd)',
        }
        error_messages = {
            'username': {
                'required': '사용자명을 입력해주세요',
            },
        }

