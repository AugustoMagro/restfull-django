from django.contrib import admin
from django.urls import path, include
from apps.academia.views import AlunoViewSet, TreinoViewSet, MatriculaViewSet, ListaMatriculaAluno, ListaMatriculaTreino
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunoViewSet, basename='Alunos')
router.register('treino', TreinoViewSet, basename='Treinos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('alunos/<int:pk>/matriculas/', ListaMatriculaAluno.as_view()),
    path('treinos/<int:pk>/matriculas/', ListaMatriculaTreino.as_view()),
]
