from django.urls import path
from curriculo import views

app_name = 'curriculo'

urlpatterns = [
    path('<str:sigla>/', views.curso, name="curso"),
    path('<str:sigla>/disciplina/<str:abr>/', views.disciplina, name="disciplina")




]  