from django.contrib import admin

# Register your models here.

from .models import Autore, Articolo

admin.site.register(Autore)
admin.site.register(Articolo)