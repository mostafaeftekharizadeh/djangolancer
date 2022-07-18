from rest_framework import viewsets
from rest_framework import authentication, permissions
from .serializers import VacancySerializer
from .models import Vacancy

# Create your views here.
class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = [permissions.IsAuthenticated]
