from django.urls import path
from . import views 
urlpatterns=[
    path('', views.home),
    path('listadoG', views.ListadoG, name = 'listadoG'),
    #path de eliminacion
    path('generoDel/<id>', views.GeneroDel, name = 'generoDel'),
    #vista template nuevo genero
    path('nuevoGenero', views.NuevoGenero, name = 'nuevoGenero'),
    #path añadir genero
    path('newGenero', views.AddGenero, name = 'guardarGenero'),
    #vista template editar genero
    path('editarGenero/<id>', views.editarGenero, name = "editarGenero"),
    path('procesarActualizacionGenero', views.procesarActualizacionGenero, name = "procesarActualizacionGenero"),

   
    path('listadoPaises', views.ListadoPaises, name = 'listadoPaises'),
    path('paisDel/<id>', views.paisDel, name = 'paisDel'),
    path('paisAddForm', views.paisAddForm, name = 'addPaises'),
    path('paisAdd', views.paisAdd, name = 'paisAdd'),
    path('paisDel/<id>', views.paisDel, name = 'paisDel'),
    path('paisEditForm/<id>', views.paisEditForm, name = 'paisEditForm'),
    path('paisUpdate', views.paisUpdate, name = "paisUpdate"),

   
   
   
   
   path('tableDirectores', views.tableDirectores, name = 'tableDirectores'),
    path('TablaFetchDirectores', views.TablaFetchDirectores, name = 'TablaFetchDirectores'),
    path('listadoDirectores', views.ListadoDirectores, name = 'listadoDirectores'), 
     path('fetchDirectores', views.fetchDirectores, name = 'fetchDirectores'), 
    path('directorDel/<id>', views.directorDel, name = 'directorDel'),
    path('directorAddForm', views.directorAddForm, name = 'directorPaises'),
    path('directorAdd', views.directorAdd, name = 'directorAdd'),
    path('directorAddFetch', views.directorAddFetch, name = 'directorAddFetch'),
    path('directorUpdateForm/<id>', views.directorUpdateForm, name = 'directorUpdateForm'),
    path('directorUpdate', views.directorUpdate, name = "directorUpdate"),


    path('listadoPeliculas', views.ListadoPeliculas),
    path('tablePeliculasFetch', views.tablePeliculasFetch, name='tablePeliculasFetch'),
    path('fetchPeliculas', views.fetchPeliculas, name='fetchPeliculas'),
    path('peliculaAddFetch', views.peliculaAddFetch, name='peliculaAddFetch'),

    path('listadoCines', views.ListadoCines, name = 'listadoCines'),
    path('addCine', views.guardarCine, name = 'addCine'),
    path('tablaCines', views.tablaCines, name = 'tablaCines'),
    #path('exportCines', views.exportCines, name = 'exportCines'),
    path('exportCinesPDF', views.exportCinesPDF, name = 'exportCinesPDF'),




]

