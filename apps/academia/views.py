from apps.academia.models import Aluno, Treino
from apps.academia.serializers import AlunoSerializer, TreinoSerializer
from rest_framework import viewsets

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class TreinoViewSet(viewsets.ModelViewSet):
    queryset = Treino.objects.all()
    serializer_class = TreinoSerializer


