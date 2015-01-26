from django import forms
from mini.web import models as m
from django.forms import ClearableFileInput


class MyClearableFileInput(ClearableFileInput):
    template_with_initial = '%(input)s'


class LoginForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Password'}),
        error_messages={'required': '비밀번호를 입력해주세요'},
        label='')

    class Meta:
        model = m.MyUser
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Username'}),
        }


class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Password'}),
        error_messages={'required': '비밀번호를 입력해주세요'},
        help_text='*',
        label='')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['email'].label = ''
        self.fields['birth'].label = ''
        self.fields['relationship_status'].label = '상태'
        self.fields['profile_image'].label = '프로필 사진'

    class Meta:
        model = m.MyUser
        fields = ('username', 'password', 'email', 'birth', 'relationship_status', 'profile_image')
        help_texts = {
            'username': '* (알파벳, 숫자, @/./+/-/_)',
            'birth': '(yyyy-mm-dd)',
        }
        error_messages = {
            'username': {
                'required': '사용자명을 입력해주세요',
            },
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'E-mail'}),
            'profile_image': MyClearableFileInput(),
            'birth': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Date of Birth'}),
            'relationship_status': forms.Select(
                attrs={'class': 'form-control'})
        }


class EditUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = 'E-mail'
        self.fields['birth'].label = '생일'
        self.fields['phone'].label = '전화번호'
        self.fields['relationship_status'].label = '상태'
        self.fields['profile_image'].label = '프로필 사진'

    class Meta:
        model = m.MyUser
        fields = ('email', 'birth', 'phone', 'relationship_status', 'profile_image')
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_image': MyClearableFileInput(),
            'birth': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'relationship_status': forms.Select(
                attrs={'class': 'form-control'}),
        }
        help_texts = {
            'birth': '(yyyy-mm-dd)',
            'profile_image': ''
        }


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = ''
        self.fields['image'].label = '사진'

    class Meta:
        model = m.Post
        fields = ('content', 'image')
        help_texts = {
        }
        error_messages = {
            'content': {
                'required': '내용을 입력해주세요.',
            },
        }
        widgets = {
            'image': MyClearableFileInput(),
            'content': forms.Textarea(attrs={'class': 'form-control',
                                             'style': 'width: 100%;'
                                                      'resize: none;'
                                                      'height: 50px;',
                                             'placeholder': "What's up?"})
        }
