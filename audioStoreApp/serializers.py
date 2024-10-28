from rest_framework import serializers
from .models import AudioStoreSaver

class AudioStoreSaverSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioStoreSaver
        fields = '__all__'
