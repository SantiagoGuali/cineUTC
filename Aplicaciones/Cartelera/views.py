import json
from django.shortcuts import render, redirect
from .models import Generos
from .models import Directores
from .models import PaisesOrigen
from .models import Pelicula, Cine
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from weasyprint import HTML
from django.template.loader import render_to_string
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "listadoGeneros.html")

#Renderizado del template de listado de generos

def ListadoG(request):
    generosBdd=Generos.objects.all()
    return render(request, "listadoG.html", {'generos':generosBdd})

#Eliminar genero por ID
def GeneroDel(request, id):
    generoDel = Generos.objects.get(id_genero = id)
    generoDel.delete()
    messages.success(request, "Género eliminado exitosamente.")
    return redirect('listadoG')


#Renderizando form de nuevo genero
def NuevoGenero(request):
    return render(request, "nuevoGenero.html")

#Insertar genero en la base de datos
def AddGenero(request):
    nom = request.POST["nombre"]
    des = request.POST["descripcion"]
    fot = request.FILES.get("foto")
    newGenero = Generos.objects.create(nombre_genero=nom, descripcion_genero=des, foto=fot)
    messages.success(request, "Género registrado exitosamente.")
    return redirect('listadoG')

#Renderizando formulario de actualizaciones 
def editarGenero(request, id):
    generoEditar = Generos.objects.get(id_genero = id)
    return render(request, "editarGenero.html", {'generoEditar' : generoEditar})

#Actualizando los nuevos datos en la BDD
def procesarActualizacionGenero(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    descripcion=request.POST['descripcion']
    fot = request.FILES.get("foto")
    generoConsultado=Generos.objects.get(id_genero = id)
    generoConsultado.nombre_genero =nombre
    generoConsultado.descripcion_genero =descripcion
    generoConsultado.foto = fot
    generoConsultado.save()
    messages.success(request,'Genero actualizado exitosamente.')
    return redirect('listadoG')



def ListadoPaises(request):
    paises = PaisesOrigen.objects.all()
    return render(request, "listadoPaises.html", {'paises':paises})

def paisDel(request, id):
    paisDel = PaisesOrigen.objects.get(id_pais = id)
    paisDel.delete()
    messages.success(request, "Pais eliminado exitosamente.")
    return redirect('listadoPaises')

def paisAddForm(request):
    return render(request, "addPaises.html")

def paisAdd(request):
    nombre=request.POST['nombre']
    continente=request.POST['continente']
    capital=request.POST['continente']
    newPais = PaisesOrigen.objects.create(nombre_pais=nombre, continente_pais = continente, capital_pais = capital)
    messages.success(request, "Pais registrado exitosamente.")
    return redirect('listadoPaises')

def paisEditForm(request, id):
    datePais = PaisesOrigen.objects.get(id_pais = id)
    return render(request, "editarPais.html", {'datePais' : datePais})

def paisUpdateForm(request, id):
    datePais = PaisesOrigen.objects.get(id_pais = id)
    return render(request, "editarGenero.html", {'datePais' : datePais})

def paisUpdate(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    continente=request.POST['continente']
    capital=request.POST['capital']
    consulta=PaisesOrigen.objects.get(id_pais = id)
    consulta.nombre_pais =nombre
    consulta.continente_pais = continente
    consulta.capital_pais =capital
    consulta.save()
    messages.success(request,'Pais actualizado exitosamente.')
    return redirect('listadoPaises')







def ListadoDirectores(request):
    directoresBdd=Directores.objects.all()
    return render(request, "listadoDirectores.html", {'directores':directoresBdd})

def directorDel(request, id):
    directorDel = Directores.objects.get(id_director = id)
    directorDel.delete()
    messages.success(request, "Director eliminado exitosamente.")
    return redirect('listadoDirectores')

def directorAddForm(request):
    return render(request, "addDirectores.html")

def fetchDirectores(request):
    return render(request, "fetchDirectores.html")

def TablaFetchDirectores(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        directores = Directores.objects.all().values('id_director','ci_director', 'apellido_director', 'nombre_director', 'estado_director')
        return JsonResponse(list(directores), safe=False)
    return JsonResponse({"error": "Invalid request"}, status=400)

def tableDirectores(request):
    return render(request, "tableDirectores.html")

def directorAddFetch(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        try:
            cedula = request.POST['ci']
            apellido = request.POST['apellido']
            nombre = request.POST['nombre']
            estado = request.POST.get('estado') == 'True'
            fot = request.FILES.get('foto_director')

            new_director = Directores.objects.create(
                ci_director=cedula, 
                apellido_director=apellido, 
                nombre_director=nombre, 
                foto_director=fot, 
                estado_director=estado
            )

            return JsonResponse({
                'estado': True,
                'mensaje': 'Director registrado exitosamente.'})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error"}, status=400)


def directorAdd(request):
    cedula=request.POST['ci']
    apellido=request.POST['apellido']
    nombre=request.POST['nombre']
    fot = request.FILES.get("foto_director")
    estado=request.POST.get('estado')
    if(request.POST.get('estado') == 'True'):
        est = True
    else:
        est = False

    newPais = Directores.objects.create(ci_director=cedula, apellido_director = apellido, nombre_director = nombre, foto_director = fot, estado_director = est)
    messages.success(request, "Director registrado exitosamente.")
    return redirect('listadoDirectores')


def directorUpdateForm(request, id):
    dateDirector = Directores.objects.get(id_director = id)
    return render(request, "editarDirectores.html", {'dateDirector' : dateDirector})

def directorUpdate(request):
    id=request.POST['id']
    cedula=request.POST['ci']
    apellido=request.POST['apellido']
    nombre=request.POST['nombre']
    fot = request.FILES.get("foto_director")
    estado=request.POST.get('estado')
   
    consulta =Directores.objects.get(id_director = id)
    consulta.ci_director = cedula
    consulta.apellido_director = apellido
    consulta.nombre_director = nombre
    consulta.foto_director = fot
    if(request.POST.get('estado') == 'True'):
        est = True
    else:
        est = False
    consulta.estado_director = est
    consulta.save()
    messages.success(request,'Director actualizado exitosamente.')
    return redirect('listadoDirectores')






def ListadoPeliculas(request):
    peliculasBdd = Pelicula.objects.all()
    return render(request, "listadoPeliculas.html", {'peliculas': peliculasBdd})

def fetchPeliculas(request):
    generos = Generos.objects.all()
    directores = Directores.objects.all()
    return render(request, "fetchPeliculas.html", {'generos': generos, 'directores': directores})

def tablePeliculasFetch(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        peliculas = Pelicula.objects.all().values('id', 'titulo', 'duracion', 'sinopsis', 'genero__nombre_genero', 'director__nombre_director')
        return JsonResponse(list(peliculas), safe=False)
    
    return JsonResponse({"error": "Invalid request"}, status=400)

def tablePeliculas(request):
    return render(request, "tablePeliculas.html")


def peliculaAddFetch(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        try:
            titulo = request.POST.get('titulo')
            duracion = request.POST.get('duracion')
            sinopsis = request.POST.get('sinopsis')
            genero_id= request.POST.get('genero')
            director_id = request.POST.get('director')
            portada = request.FILES.get('portada')
            genero = Generos.objects.get(id_genero=genero_id)
            director = Directores.objects.get(id_director=director_id)

            nueva_pelicula = Pelicula(
                titulo=titulo,
                duracion=duracion,
                sinopsis=sinopsis,
                genero=genero,
                director=director,
                portada=portada
            )
            nueva_pelicula.save()
            return JsonResponse({
                'estado': True,
                'mensaje': 'Cine registrado exitosamente.'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)









def ListadoCines(request):
    return render(request, 'listadoCines.html')

#Insertando cines mediante AJAX en la Base de Datos
@csrf_exempt
def guardarCine(request):
    nom=request.POST["nombre"]
    dir=request.POST["direccion"]
    tel=request.POST["telefono"]
    nuevoCine=Cine.objects.create(nombre=nom,direccion=dir,telefono=tel)    
    return JsonResponse({
        'estado': True,
        'mensaje': 'Pelicula registrado exitosamente.'
    })


def ListadoCines(request):
    dataCines = Cine.objects.all()
    return render(request,"listadoCines.html", {'cines': dataCines})

def tablaCines(request):
    dataCines = Cine.objects.all()
    return render(request,"tablaCines.html", {'cines': dataCines})

def exportCines(request):
    dataCines = Cine.objects.all()
    return render(request,"exportCines.html", {'cines': dataCines})


#---------------------------------------------------------------------------------------------------------------------
def exportCinesPDF(request):
    #llamar a todos los datos del modelo cina
    cines = Cine.objects.all()
    #llamar al template con el render string
    html_string = render_to_string('exportCines.html', {'cines': cines})
    #almacenar como un archivo html
    html = HTML(string=html_string)
    #leer todo el html guardado y convvertirlo en un pdf
    pdf = html.write_pdf()
    #dar una respuesta como pdf(archivo)
    response = HttpResponse(pdf, content_type='application/pdf')
    #nombrar y dar una extension al archivo expotado
    response['Content-Disposition'] = 'attachment; filename="reporte_cines.pdf"'
    #exportar archivo
    return response




