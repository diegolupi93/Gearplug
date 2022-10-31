from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Character
from .serializers import CharacterSerializer, MovieSerializer, PlanetSerializer
from rest_framework import generics
from django.db import IntegrityError
from django.core.exceptions import ValidationError


# Hacer una viewset de character
class CharacterViewSet(viewsets.ModelViewSet):
    """
    List and Post Characters.
    """
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    
    def perform_create(self, serializer):
        try:
            serializer.save()
        except IntegrityError:
            raise ValidationError('Character with this Name and User already exists.')

class MovieCreate(generics.CreateAPIView):
    """Post Movies"""
    serializer_class = MovieSerializer

class PlanetCreate(generics.CreateAPIView):
    """Post Planets"""
    serializer_class = PlanetSerializer

