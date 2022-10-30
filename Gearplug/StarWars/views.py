from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Character
from .serializers import CharacterSerializer, MovieSerializer, PlanetSerializer
from rest_framework import generics



# Hacer una viewset de character
class CharacterViewSet(viewsets.ModelViewSet):
    """
    List and Post Characters.
    """
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']


class MovieCreate(generics.CreateAPIView):
    """Post Movies"""
    serializer_class = MovieSerializer

class PlanetCreate(generics.CreateAPIView):
    """Post Planets"""
    serializer_class = PlanetSerializer

