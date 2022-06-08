from django.contrib import admin

# Register your models here.

from .models import Sensor, Detection

class DetectionAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ('Sensore',               {'fields': ['sensor']}),
        ('Parametri', {'fields': ['timestamp','value']}),
    ]
    
    list_display = ('sensor', 'timestamp', 'value')

admin.site.register(Sensor)
admin.site.register(Detection, DetectionAdmin)

