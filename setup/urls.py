from django.contrib import admin
from django.urls import path, include
from apps.academia.views import AlunoViewSet, TreinoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunoViewSet, basename='Alunos')
router.register('treino', TreinoViewSet, basename='Treinos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
