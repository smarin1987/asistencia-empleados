from django.urls import path
from . import views

urlpatterns = [
    path('', views.marcar_asistencia),
]
