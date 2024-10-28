from rest_framework import serializers
from .models import VideoLoader

class VideoLoaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoLoader
        fields = '__all__'  # Vous pouvez aussi spécifier les champs manuellement
