from django.urls import path
from . views import ListaDirectores

app_name = 'directores'

urlpatterns = [
    path('',ListaDirectores.as_view(), name = 'home')
]
