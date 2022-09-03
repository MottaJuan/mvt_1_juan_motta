from django.http import HttpResponse
from django.template import Template, Context, loader
from familiares.models import Familiares


def listar(request):
    queryset=Familiares.objects.all()
    diccionario={'familiares':queryset}
    plantilla=loader.get_template('familiares_list.html')
    documento_html=plantilla.render(diccionario)
    return HttpResponse(documento_html)
