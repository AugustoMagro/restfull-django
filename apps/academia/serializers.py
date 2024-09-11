from rest_framework import serializers
from apps.academia.models import Aluno, Treino

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'name', 'email', 'date_born', 'phone']

class TreinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treino
        fields = '__all__'