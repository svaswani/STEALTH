from django import forms
from tools.models import Post, BaseUser, Comment
from django.contrib.auth.forms import UserCreationForm
from django.forms import PasswordInput
from django.forms import ModelForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        title = forms.CharField()
        description = forms.CharField()
        fields = ['title', 'description']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment']

class accountCreation(UserCreationForm):

    class Meta:
        model = BaseUser
        fields = ['username', 'email']
        widgets = {
            'password': PasswordInput(render_value=True),
        }

    def __init__(self, *args, **kwargs):
        """
        Makes input from user for all fields in form required
        """
        super(ModelForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].required = True
            self.fields[key].help_text = None
