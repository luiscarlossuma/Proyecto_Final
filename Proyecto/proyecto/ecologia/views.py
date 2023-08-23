from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect

from .models import Reportes
from .forms import ReporteForm

def index(request):

    return HttpResponse("Este es el proyecto de la secretaria de ecologia")

class Inicio(View):
    template_name = 'inicio.html'

    def post():

        return

    def get(self, request):
        # Esta es mi clase GET #
        print('Ya inició mi GET-----*')

        return render(request, self.template_name)

class Crear(View):
    template_name = 'reportes/crear.html'

    def post(self, request):
        form = ReporteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear')
        return render(request, self.template_name, {'form': form})

    def get(self, request):
        form = ReporteForm()
        return render(request, self.template_name, {'form': form})