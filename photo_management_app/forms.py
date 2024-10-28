from photo_management_app.models import PhotoModel

from django import forms


class PhotoForm(forms.ModelForm):
    class Meta:
        model = PhotoModel
        fields = ['image','caption']