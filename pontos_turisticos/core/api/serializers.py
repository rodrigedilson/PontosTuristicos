from rest_framework import serializers
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer


class PontoTuristicoSerializer(serializers.ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()
    descricao_completa = serializers.SerializerMethodField()
    
    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'endereco', 'atracoes',
                  'aprovado', 'foto', 'descricao_completa', 'descricao_completa2')
        
    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)