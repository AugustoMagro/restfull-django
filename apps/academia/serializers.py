from rest_framework import serializers
from apps.academia.models import Aluno, Treino, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'name', 'email', 'date_born', 'phone']

class TreinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treino
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'

class listaMatriculasAlunosSerializer(serializers.ModelSerializer):
    treino = serializers.ReadOnlyField(source='treino.descricao')
    plano = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['treino','plano']
    def get_plano(self, obj):
        return obj.get_plano_display()
    
class listaMatriculasTreinoSerializer(serializers.ModelSerializer):
    nome_aluno = serializers.ReadOnlyField(source='aluno.name')
    class Meta:
        model = Matricula
        fields = ['nome_aluno']