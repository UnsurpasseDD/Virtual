from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Users
        fields = ['email', 'first_name', 'last_name', 'patronymic', 'id', 'phone']

class CoordsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height']

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'spring', 'summer','autumn']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['image', 'title']

class PerevalSerializer(serializers.ModelSerializer):
    turist_id = UserSerializer()
    coords_id = Coords()
    level = LevelSerializer()
    images = ImageSerializer()
    add_time = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S')

    class Meta:
        model = Pereval
        fields = ['beauty_title', 'title', 'other_titles', 'connect', 
                  'add_time', 'turist_id', 'status', 'level', 'coords_id','images']
        
    def create(self, validated_data, **kwargs):
        tourist_id = validated_data.pop('tourist_id')
        coords_id = validated_data.pop('coords_id')
        level = validated_data.pop('level')
        images = validated_data.pop('images')

        user, created = Users.objects.get_or_create(**user)
        tourist_id, created= Users.objects.get_or_create(**tourist_id)
            
        coords_id = Coords.objects.create(**coords_id)
        level = Level.objects.create(**level)
        pereval = Pereval.objects.create(**validated_data, tourist_id=tourist_id, coords_id=coords_id, level=level, status='NW')

        for i in images:
            image = i.pop('image')
            title = i.pop('title')
            Images.objects.create(image=image, pereval_id=pereval, title=title)
            
        return pereval
        
    def validare(self, data):
        if self.instance is not None:
            instance_user=self.instance.user
            data_user = data.get('user')
            validating_user_fields=[
                instance_user.last_name != data_user['last_name'],
                instance_user.first_name != data_user['first_name'],
                instance_user.patronymic != data_user['patronymyc'],
                instance_user.email != data_user['email']
                 
                 ] 
            if data_user is not None and any(validating_user_fields):
                raise serializers.ValidationError({'Отклонено': 'Нельзя изменять данные пользователя'})
            
        return data
