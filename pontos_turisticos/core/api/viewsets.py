from rest_framework import viewsets
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework import filters
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication


class PontoTuristicoViewSet(viewsets.ModelViewSet):
    #queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'descricao', 'endereco__linha1']
    #lookup_field = 'nome'
    #permission_classes = [DjangoModelPermissions]
    #authentication_classes = [TokenAuthentication]
    
    def get_queryset(self):
        queryset = PontoTuristico.objects.all()
        
        #id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        #descricao = self.request.query_params.get('descricao', None)
        
        #if id is not None:
            #queryset = queryset.filter(id__iexact=id)
            
        if nome is not None:
            queryset = queryset.filter(nome__iexact=nome)
            
        #if descricao is not None:
            #queryset = queryset.filter(descricao__iexact=descricao)
        
        return queryset