"""
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

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
"""