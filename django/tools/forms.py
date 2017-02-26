from django import forms
from tools.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        title = forms.CharField()
        description = forms.CharField()
        fields = ['title', 'description']
