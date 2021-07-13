from rest_framework import viewsets
from atracoes.models import Atracao
from atracoes.api.serializers import AtracaoSerializer


class AtracaoViewSet(viewsets.ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer