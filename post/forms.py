from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('name', 'content', 'expiry_date')
        widgets = {
            'name': forms.fields.TextInput(attrs={
                'placeholder': 'Post Title',
                'class': 'form-control',
                'required': 'true'
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Post Content',
                'class': 'form-control',
                'required': 'true'
            }),
            'expiry_date': forms.fields.DateInput(attrs={
                'type': 'date',
                'placeholder': 'Date of Expiry',
                'class': 'form-control'
            })
        }
        error_messages = {
            'name': {'required': "The post title can't be empty",
                     'unique': "You can't have two posts with the same name"},
            'content': {'required': "The post content can't be empty"}
        }
