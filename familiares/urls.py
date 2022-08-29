from django.urls import path
from familiares.views import listar


urlpatterns = [
    path('', listar),
]
