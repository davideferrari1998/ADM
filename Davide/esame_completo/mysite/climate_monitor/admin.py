from django.contrib import admin

# Register your models here.

from django.contrib import admin
# Register your models here.
from .models import Sensor, Detection

admin.site.register(Sensor)
admin.site.register(Detection)
