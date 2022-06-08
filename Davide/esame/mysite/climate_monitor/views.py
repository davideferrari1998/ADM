from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from .models import Sensor, Detection


def index(request):
    return HttpResponse("Hello, world. You're at the Climate Monitor index.")

def LetturaView(request, tipo_lettura):
    l = []
    sensori = Sensor.objects.filter(type = tipo_lettura)
    
    for x in sensori:
        val = 0
        num = 0

        d = Detection.objects.filter(sensor = x)

        for i in d:

            if i.is_valid():
                val = i.value + val
                num = num + 1
                val = val / num

        if num != 0:
            l.append({'id':x.id,'address': x.address, 'CAP': x.CAP, 'val':val})
        
    
    return render(request, 'climate_monitor/detections.html',{'detec': l})