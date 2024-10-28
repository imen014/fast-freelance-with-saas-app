from audioStoreApp.models import AudioStoreSaver
from django import forms


class AudioForm(forms.ModelForm):
    class Meta:
        model = AudioStoreSaver
        fields = ['audio','text','image']