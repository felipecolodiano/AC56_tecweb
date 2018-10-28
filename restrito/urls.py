from django.urls import path
from restrito import views

app_name = 'restrito'

urlpatterns = [
    path('<str:nome>/', views.restrito, name="perfis"),
]  