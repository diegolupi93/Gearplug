from enum import Flag
from urllib import response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Character, Movie, Planet
from .serializers import CharacterSerializer, MovieSerializer, PlanetSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework import permissions


class CharacterCreated(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        exist_character = Character.objects.filter(**request.data).exists()
        if exist_character:
            return False
        #import ipdb
        #ipdb.set_trace()
        return True

# Hacer una viewset de character
class CharacterViewSet(viewsets.ModelViewSet):
    """
    List and Post Characters.
    """
    permission_classes = [CharacterCreated]
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

