from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'character', views.CharacterViewSet, basename='characterList')
view_patterns = [
    path('movie/', views.MovieCreate.as_view(), name='MovieCreate'),
    path('planet/', views.PlanetCreate.as_view(), name='PlanetCreate'),
    ]
urlpatterns = router.urls + view_patterns

