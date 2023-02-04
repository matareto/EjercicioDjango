# Create your views here.
from django.shortcuts import render
from directores.models import Director, Peliculas
from django.views.generic import View

class ListaDirectores(View):
    def get(self,request):
        directores = Director.objects.all()
        num_direc_reg = Director.objects.all().count()
        num_pelis_reg = Peliculas.objects.all().count()
        peliculas = Peliculas.objects.all()
        context = {
            'directores':directores,
            'num_direc_reg':num_direc_reg,
            'num_pelis_reg':num_pelis_reg,
            'peliculas':peliculas
        }
        
        return render(request,"lista_directores.html",context)
