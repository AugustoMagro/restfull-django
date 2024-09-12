from apps.academia.models import Aluno, Treino, Matricula
from apps.academia.serializers import AlunoSerializer, TreinoSerializer, MatriculaSerializer, listaMatriculasAlunosSerializer, listaMatriculasTreinoSerializer
from rest_framework import viewsets, generics

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class TreinoViewSet(viewsets.ModelViewSet):
    queryset = Treino.objects.all()
    serializer_class = TreinoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculaAluno(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = listaMatriculasAlunosSerializer

class ListaMatriculaTreino(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(treino_id=self.kwargs['pk'])
        return queryset
    serializer_class = listaMatriculasTreinoSerializer