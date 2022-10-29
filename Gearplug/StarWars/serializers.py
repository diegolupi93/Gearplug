from django.db.models import fields
from rest_framework import serializers
from .models import Character, Movie, Planet, Productor


class ProductorSerializer(serializers.ModelSerializer):
    movies = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Productor
        fields = ('name', 'movies')
        read_only_fields = ['movies']

class PlanetSerializer(serializers.ModelSerializer):
    movies = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Planet
        fields = ('name', 'galaxy', 'movies')
        read_only_fields = ['movies'] 

class CharacterMoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('name', 'description', 'director')


class CharacterSerializer(serializers.ModelSerializer):
    movies = CharacterMoviesSerializer(many=True, read_only=True)
    class Meta:
        model = Character
        fields = ('name', 'age', 'movies')
        read_only_fields = ['movies']


class MovieSerializer(serializers.ModelSerializer):
    characters = CharacterSerializer(many=True)
    productors = ProductorSerializer(many=True)
    planets = PlanetSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('name', 'description', 'director', 'productors', 'characters', 'planets')

    def create(self, validated_data):
        planets_data = validated_data.pop('planets')
        productors_data = validated_data.pop('productors')
        characters_data = validated_data.pop('characters')
        exist_movie = Movie.objects.filter(**validated_data).exists()
        movie = Movie.objects.create(**validated_data)
    
        for character in characters_data:
            created = Character.objects.filter(**character).exists()
            if not (exist_movie and created):
                character_obj, created = Character.objects.get_or_create(**character)
                movie.characters.add(character_obj)
        
        for planet in planets_data:
            created = Planet.objects.filter(**planet).exists()
            if not (exist_movie and created):
                planet_obj, created = Planet.objects.get_or_create(**planet)
                movie.planets.add(planet_obj)
            
        
        for productors in productors_data:
            created = Productor.objects.filter(**productors).exists()
            if not (exist_movie and created):
                productor_obj, created = Productor.objects.get_or_create(**productors)
                movie.productors.add(productor_obj)

        return movie
    