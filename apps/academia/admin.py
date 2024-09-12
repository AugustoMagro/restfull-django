from django.contrib import admin
from apps.academia.models import Aluno, Treino, Matricula

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'cpf', 'date_born', 'phone',)
    list_display_links = ('id', 'name',)
    list_per_page = 20
    search_fields = ('name',)

admin.site.register(Aluno, Alunos)

class Treinos(admin.ModelAdmin):
    list_display = ('id', 'name', 'descricao', 'nivel',)
    list_display_links = ('id', 'name',)
    search_fields = ('name','nivel',)

admin.site.register(Treino, Treinos)

class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'treino', 'plano',)
    list_display_links = ('id',)

admin.site.register(Matricula, Matriculas)

