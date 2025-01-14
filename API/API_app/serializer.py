from rest_framework import serializers
from .models import Video, Image

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
    def create(self, validated_data):
        return Video.objects.create(**validated_data)
    
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
    def create(self, validated_data):
        return Image.objects.create(**validated_data)

'''
class VideoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    videoURL = serializers.FileField()
    description = serializers.CharField()
    date = serializers.DateTimeField() 

class ImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    imageURL = serializers.ImageField()
    description = serializers.CharField()
    date = serializers.DateTimeField()
'''