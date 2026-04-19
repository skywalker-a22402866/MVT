
from django.urls import path
from .views import cursos_view

urlpatterns = [
    path('cursos/', cursos_view, name='cursos'),
]