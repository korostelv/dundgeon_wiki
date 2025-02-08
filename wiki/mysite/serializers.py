from rest_framework import serializers
from .models import Release, Race, Personage, Gamer, Storyline


class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        fields = '__all__'


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = '__all__'


class PersonageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personage
        fields = '__all__'


class GamerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gamer
        fields = '__all__'


class StorylineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storyline
        fields = '__all__'