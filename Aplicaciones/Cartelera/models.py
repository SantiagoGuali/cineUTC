from django.db import models

# Create your models here.
class Generos(models.Model):
    id_genero=models.AutoField(primary_key=True)
    nombre_genero=models.CharField(max_length=25)
    descripcion_genero = models.CharField(max_length=150,default="")
    foto = models.FileField(upload_to='generos', null=True, blank=True)

    def __str__(self):
        fila="{0}: {1} - {2}" 
        return fila.format(self.id_genero,self.nombre_genero, self.descripcion_genero)

class Directores(models.Model):
    id_director = models.AutoField(primary_key=True)
    ci_director = models.CharField(max_length=15)
    apellido_director = models.CharField(max_length=50)
    nombre_director = models.CharField(max_length=50)
    foto_director = models.FileField(upload_to='directores', null=True, blank=True)
    estado_director = models.BooleanField(default=True)

    def __str__(self):
        fila="{0}: {1} - {2} - {3} - {4}"
        return fila.format(self.id_director,self.ci_director,self.apellido_director,self.nombre_director,self.estado_director)
    
class PaisesOrigen(models.Model):
    id_pais = models.AutoField(primary_key=True)
    nombre_pais = models.CharField(max_length=50)
    continente_pais = models.CharField(max_length=50)
    capital_pais = models.CharField(max_length=50)

    def __str__(self):
        fila="{0}: {1} - {2} - {3}"
        return fila.format(self.id_pais, self.nombre_pais, self.continente_pais, self.capital_pais)


class Pelicula(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=250)
    duracion = models.TimeField(null=True)
    sinopsis = models.TextField()
    genero = models.ForeignKey(Generos, on_delete=models.CASCADE)
    director = models.ForeignKey(Directores, on_delete = models.CASCADE)
    portada = models.FileField(upload_to='generos', null=True, blank=True)

    def __str__(self):
        fila = "{0} : {1} - {2} - {3} - {4}"
        return fila.format(self.id, self.titulo, self.duracion, self.genero, self.director)
    
    #Creando modelo Cine
class Cine(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=25)
    direccion=models.CharField(max_length=150,default='')
    telefono=models.CharField(max_length=150,default='')
    def __str__(self):
        fila="{0}: {1} - {2}"
        return fila.format(self.id,self.nombre,self.direccion)