from rest_framework import viewsets
from app.models import Hero
from app.serializers import HeroSerializer

class HeroViewSets(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer