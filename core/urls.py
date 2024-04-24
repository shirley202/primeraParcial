from django.urls import path
from . import views

urlpatterns = [
    path('importar-pdf/', views.importar_pdf, name='importar_pdf'),
    path('import-success/', views.import_success, name='import_success'),
    path('seleccionar-carrera/', views.seleccionar_carrera, name='seleccionar_carrera'),
    path('ver-programa/<str:carrera>/', views.ver_programa, name='ver_programa'),


]
