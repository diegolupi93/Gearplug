from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from .models import Character, Movie, Planet
from .serializers import CharacterSerializer, MovieSerializer, PlanetSerializer
import json
from rest_framework import status

# Create your tests here.
# List
class GetAllCharactersTest(TestCase):
    """ Test module for GET all characters API """
    
    def setUp(self):
        Character.objects.create(
            name='Casper', age=3)
        Character.objects.create(
            name='Muffin', age=1)
        Character.objects.create(
            name='Rambo', age=2)
        Character.objects.create(
            name='Ricky', age=6)

    def test_get_all_characters(self):
        # get API response
        response = self.client.get(reverse('characterList-list'))
        # get data from db
        character = Character.objects.all()
        serializer = CharacterSerializer(character, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# Hacer lo mismo con Planet y Movie
class CreateNewCharacterTest(TestCase):
    """ Test module for inserting a new Character """

    def setUp(self):
        self.valid_payload = {
            'name': 'Muffin',
            'age': 4
        }
        self.invalid_payload = {
            'name': "",
            'age': 4,
        }

    def test_create_valid_character(self):
        client = APIClient()
        response = self.client.post(
            '/starwars/',
            self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_character(self):
        response = self.client.post(
            '/starwars/',
            self.invalid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

