from django.urls import path
from apps.indicadores.views import index, welcome

urlpatterns = [
    path('', welcome),
    path('indicadores/', index, name='index')
]
