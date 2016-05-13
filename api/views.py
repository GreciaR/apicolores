from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Color
from .forms import ColorForm

# Create your views here.

def index(request):
    return HttpResponse('Hola')

class HomeView(View):
    def get(self, request):
        return HttpResponse("home")

class IndexView(View):
    def get(self, request):
        get_params = request.GET
        nombre = get_params.get('nombre', 'fulano')
        return HttpResponse("<h1>HOla" + nombre + "<h1>")


@csrf_exempt
def prueba(request):
    return HttpResponse("hola post")

class GreetView(View):
    def get(self, request, nombre):
        return HttpResponse("<h1> HOla + nombre <h1>")

"""
Esta vista intenta renderizar un json
"""

class JsonView(View):
    def get(self, request):
        return HttpResponse("""
            {"grupo: "Cinta negra", "integrantes":["salvador", "ivan", "hector"]}""", content_type='application/json')

    def post(self, request):
        my_json ={
            'colors': [
                '#000000',
                '#FFFFFF',
                '#FF0000',
            ]
        }
        color = request.POST.get('color')
        if color:
            my_json['colors'].append(color)
        return HttpResponse(json.dumps(my_json), content_type='application/json')

class ColorView(View):
    colores = {
            'rojo': '#FF0000',
            'azul': '#0000FF'
    }
    def get(self, request, color):
        hex = self.colores.get(color)
        if hex:
            resp = {'status': 'ok', 'hex': hex }
        else:
            resp = {'status': 'error', 'message': 'no disponible'}

        return HttpResponse(json.dumps(resp), content_type='application/json')

class ColorsView(View):
    def get(self, request):
            list_colors = []
            colors = Color.objects.all()
            for c in colors:
                dic_colors = {
                    'name' : c.name,
                    'hexadecimal' : c.hexadecimal,
                    'red' : c.red,
                    'green' : c.green,
                    'blue' : c.blue,
                }
                list_colors.append(dic_colors)
            my_colorsjson = {'colors' : list_colors}
            return HttpResponse(json.dumps(my_colorsjson), content_type='application/json')

class Home(View):
    def get(self,request):
        template_name='formulario.html'
        form = ColorForm()
        context={
        'form': form
        }
        return render (request, template_name, context)

    def post(self, request):
        color = ColorForm(request.POST)
        if color.is_valid(): 
            color = color.save()
            return HttpResponse("OK")
        else:
            return HttpResponse("esta mal")

class Paleta(View):
    def get(self, request):
        template_name='paleta.html'
        form = PaletaForm()
        context={
        'form': form
        }
        return render (request, template_name, context)

    def porst(self, request):
        paleta = paleta.save


