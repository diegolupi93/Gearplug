from django.db.models import fields
from rest_framework import serializers
from .models import Character, Movie, Planet, Productor

class CharacterSerializer(serializers.ModelSerializer):
    movies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Character
        fields = ('name', 'age', 'movies')
        read_only_fields = ['movies']

class ProductorSerializer(serializers.ModelSerializer):
    movies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Productor
        fields = ('name', 'movies')
        read_only_fields = ['movies']

class PlanetSerializer(serializers.ModelSerializer):
    movies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Planet
        fields = ('name', 'galaxy', 'movies')
        read_only_fields = ['movies'] 

class MovieSerializer(serializers.ModelSerializer):
    characters = CharacterSerializer(Character.objects.all(), many=True)
    productors = ProductorSerializer(Character.objects.all(), many=True)
    planets = PlanetSerializer(Planet.objects.all(), many=True)
    
    
    class Meta:
        model = Movie
        fields = ('name', 'description', 'director', 'productors', 'characters', 'planets')

    def create(self, validated_data):
        characters_data = validated_data.pop('characters')
        planets_data = validated_data.pop('planets')
        productors_data = validated_data.pop('productors')
        movie = Movie.objects.create(**validated_data)

        for characters in characters_data:
            Character.objects.create(movie=movie, **characters)
        
        for planets in planets_data:
            Planet.objects.create(movie=movie, **planets)
        
        for productors in productors_data:
            Planet.objects.create(movie=movie, **productors)

        return movie
    