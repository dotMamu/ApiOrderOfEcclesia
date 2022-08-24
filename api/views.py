
# importe para renderizar vistas, importado por defecto 
from django.shortcuts import render

# importes necesarios para respuesta
from django.http.response import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

#importe de modelos necesarios
from .models import *

# Create your views here.


class Weapons(View):

    @method_decorator(csrf_exempt) 
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, name=''):
        if name!='':
            weapons = list(Weapon.objects.filter(name=name).values())
            if len(weapons) > 0:
                datos = {"message": "Success", "companies": weapons}
            else:
                datos = {"message": "An error ocurred"}
            return JsonResponse(datos)
        else:
            companies = list(Weapon.objects.values())
            if len(companies) > 0:
                datos = {"message": "Success", "companies": companies}
            else:
                datos = {"message": "Companies not found"}
            return JsonResponse(datos)
    

    def post(self, request,item1,item2):
        #print(request.body)
        jd = json.loads(request.body)
        #print(jd)
        Weapon.objects.create(name=jd['name'], website=jd['website'], foundation=jd['foundation'])
        datos = {"message": "Success"}
        return JsonResponse(datos)

class Glyph_Union(View):
    def get(self, request, item1,item2):
        


        pass
