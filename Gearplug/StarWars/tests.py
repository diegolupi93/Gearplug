from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django.urls import reverse
from .models import Character
from .serializers import CharacterSerializer

from rest_framework import status
from rest_framework.test import force_authenticate
from .views import CharacterViewSet, PlanetCreate, MovieCreate

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
        factory = APIRequestFactory()
        view = CharacterViewSet.as_view({'post':'create'})
        request = factory.post(
            '/starwars/character/',
            self.valid_payload,
            format='json'
        )
        force_authenticate(request)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_character(self):
        factory = APIRequestFactory()
        view = CharacterViewSet.as_view({'post':'create'})
        request = factory.post(
            '/starwars/character/',
            self.invalid_payload,
            format='json'
        )
        force_authenticate(request)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class CreateNewPlanetTest(TestCase):
    """ Test module for inserting a new Planet """

    def setUp(self):
        self.valid_payload = {
            'name': 'Muffin',
            'galaxy': 'Andromeda'
        }
        self.invalid_payload = {
            'name': "pluton",
            'galaxy': "",
        }

    def test_create_valid_planet(self):
        factory = APIRequestFactory()
        view = PlanetCreate.as_view()
        request = factory.post(
            '/starwars/planet/',
            self.valid_payload,
            format='json'
        )
        force_authenticate(request)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_planet(self):
        factory = APIRequestFactory()
        view = PlanetCreate.as_view()
        request = factory.post(
            '/starwars/planet/',
            self.invalid_payload,
            format='json'
        )
        force_authenticate(request)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class CreateNewMovieTest(TestCase):
    """ Test module for inserting a new Movie """

    def setUp(self):
        self.valid_payload = {
                                "name": "La amenaza fantasma",
                                "description": "Larga",
                                "director": "George Lucas",
                                "productors": [
                                    {
                                        "name": "Jorge"
                                    },
                                    {
                                        "name": "Pedro"
                                    }
                                ],
                                "characters": [
                                    {
                                        "name": "Yoda",
                                        "age": 100
                                    },
                                    {
                                        "name": "Obi-Wan",
                                        "age": 30
                                    }
                                ],
                                "planets": [
                                    {
                                        "name": "Pluton",
                                        "galaxy": "Via Lactea"
                                    }
                                ]
                            }
        self.invalid_payload = {
                                "name": "",
                                "description": "Buena",
                                "director": "George Lucas",
                                "productors": [
                                    {
                                        "name": "Jorge"
                                    },
                                    {
                                        "name": "Pedro"
                                    }
                                ],
                                "characters": [
                                    {
                                        "name": "pepe",
                                        "age": 21
                                    },
                                    {
                                        "name": "El yohni",
                                        "age": 30
                                    }
                                ],
                                "planets": [
                                    {
                                        "name": "Pluton",
                                        "galaxy": "Via Lactea"
                                    }
                                ]
                            }

    def test_create_valid_movie(self):
        factory = APIRequestFactory()
        view = MovieCreate.as_view()
        request = factory.post(
            '/starwars/movie/',
            self.valid_payload,
            format='json'
        )
        force_authenticate(request)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_movie(self):
        factory = APIRequestFactory()
        view = MovieCreate.as_view()
        request = factory.post(
            '/starwars/movie/',
            self.invalid_payload,
            format='json'
        )
        force_authenticate(request)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)