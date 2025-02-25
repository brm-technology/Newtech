from rest_framework import serializers
from .models import Picture

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ['id', 'Img_name', 'Image', 'shape', 'x_cor', 'y_cor', 'z_cor', 'Prefillcolor', 'Date']


