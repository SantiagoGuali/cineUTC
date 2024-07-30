from django.contrib import admin
from .models import Generos
from .models import Directores
from .models import PaisesOrigen
from .models import Pelicula
# Register your models here.
admin.site.register(Generos)
admin.site.register(Directores)
admin.site.register(PaisesOrigen)
admin.site.register(Pelicula)