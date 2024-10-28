from django import forms

from Blogger.models import ImageModel, BlogModel


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields=['image']


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['blog_title','blog_content']