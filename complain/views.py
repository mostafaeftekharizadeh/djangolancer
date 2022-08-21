from django.shortcuts import render
from .models import Complain,ResultComplain
from .serializers import ComplainSerializer,ResultComplain

# Create your views here.
class ComplainViewSet(viewsets.ModelViewSet):
    queryset = Complain.objects.all()
    serializer_class = ComplainSerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)

class ResultComplainViewSet(viewsets.ModelViewSet):
    queryset = ResultComplain.objects.all()
    serializer_class = ResultComplainSerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)