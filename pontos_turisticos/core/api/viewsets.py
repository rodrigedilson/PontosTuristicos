from rest_framework import viewsets
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(viewsets.ModelViewSet):
    #queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    
    def get_queryset(self):
        queryset = PontoTuristico.objects.filter(aprovado=True)
        
        return queryset