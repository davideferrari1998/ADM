from django.contrib import admin
from .models import Sensori, Rilevamenti

# Register your models here.
class RilevamentiAdmin(admin.ModelAdmin):
    list_display = ('sensore', 'timestamp', 'type')


admin.site.register(Sensori)
admin.site.register(Rilevamenti, RilevamentiAdmin)
