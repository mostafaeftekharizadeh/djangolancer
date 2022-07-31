from rest_framework import viewsets
from rest_framework import authentication, permissions
from .serializers import VacancySerializer, SkillSerializer, CategorySerializer, LevelSerializer,PlaceSerializer,CountrySerializer,StateSerializer,CitySerializer,EstimateSerializer
from .models import Vacancy, Skill, Category,Place, Level,Country,State,City,Estimate
from rest_framework import generics
from django_filters import rest_framework as filters



# Create your views here.

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)
class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)
class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('country', 'state', 'city', 'skills', 'user', 'level', 'place')
    '''
    filter vacancies based on owner
    '''
    def get_queryset(self):
        if self.request.GET.get('owner') == '1':
            return Vacancy.objects.filter(user=self.request.user)
        else:
            return Vacancy.objects.all().exclude(user=self.request.user)


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)
class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)


class EstimateViewSet(viewsets.ModelViewSet):
    queryset = Estimate.objects.all()
    serializer_class = EstimateSerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)
