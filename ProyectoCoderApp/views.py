from django.shortcuts import render, HttpResponse
from .models import Familiar
from django.template import loader

# Create your views here.


def familiar(request):

    familiar1 = Familiar(
        nombre="Maximiliano", apellido="Viltre", edad=37, fecha_nacimiento="1985-06-26"
    )
    familiar1.save()

    familiar2 = Familiar(
        nombre="Martin", apellido="Viltre", edad=35, fecha_nacimiento="1987-03-01"
    )
    familiar2.save()

    familiar3 = Familiar(
        nombre="David", apellido="Viltre", edad=32, fecha_nacimiento="1989-05-02"
    )
    familiar3.save()

    plantilla = loader.get_template("Template1.html")

    familiares = {"familiares": [familiar1, familiar2, familiar3]}

    documento = plantilla.render(familiares)

    return HttpResponse(documento)
