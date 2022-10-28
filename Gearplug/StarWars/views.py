from urllib import response
import django_filters.rest_framework
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Character, Movie, Planet
from .serializers import CharacterSerializer, MovieSerializer, PlanetSerializer
from rest_framework.decorators import api_view
from rest_framework import generics

# Hacer una viewset de character
class CharacterViewSet(viewsets.ViewSet):
    """
    Coment
    """
    def list(self, request):
        queryset = Character.objects.all()
        serializer = CharacterSerializer(queryset, many=True)
        filterset_fields = ['name']
        return Response(serializer.data)
    
    def create(self, request):
        serializer = CharacterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class CharacterList(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    filterset_fields = ['name']

class CharacterCreate(generics.CreateAPIView):
    serializer_class = CharacterSerializer

class MovieCreate(generics.CreateAPIView):
    serializer_class = MovieSerializer

class PlanetCreate(generics.CreateAPIView):
    serializer_class = PlanetSerializer

