from django import forms
from videoStoreApp.models import VideoLoader


class VideoForm(forms.ModelForm):
    class Meta:
        model = VideoLoader
        fields = ['video','titre','creator']