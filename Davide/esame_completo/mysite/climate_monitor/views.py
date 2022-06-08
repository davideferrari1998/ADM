from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Sensor, Detection
from django.views import generic
from django.contrib.auth.decorators import login_required 

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the Climate Monitor index.")

def LetturaView(request, tipo_lettura):
    l = []
    sens = Sensor.objects.filter(type=tipo_lettura)

    for s in sens:
        val = 0
        num = 0
        d = Detection.objects.filter(sensor = s)

        for i in d:
            if i.is_valid():
                val = val + i.value
                num = num + 1

        if num != 0:
            val = val / num
            l.append({'id': s.id, 'type': s.type, 'address': s.address, 'CAP': s.CAP, 'val': val})       

    return render(request, 'climate_monitor/detection.html',{'detec': l})

@login_required
def LetturaViewJSON(request, tipo_lettura):
    l = []
    sens = Sensor.objects.filter(type=tipo_lettura)

    for s in sens:
        val = 0
        num = 0
        d = Detection.objects.filter(sensor = s)

        for i in d:
            if i.is_valid():
                val = val + i.value
                num = num + 1

        if num != 0:
            val = val / num
            l.append({'id': s.id, 'type': s.type, 'address': s.address, 'CAP': s.CAP, 'val': val})       

    return JsonResponse({'detec': l})

class SensorFormView(generic.edit.CreateView):
    model = Sensor
    template_name = 'climate_monitor/form.html'
    fields = '__all__'
    
    success_url = '/climate_monitor/'

class SensorFormModify(generic.edit.UpdateView):
    model = Sensor
    template_name = 'climate_monitor/form.html'
    fields = '__all__'
    
    success_url = '/climate_monitor/'

class SensorFormDelete(generic.edit.DeleteView):
    model = Sensor
    success_url = '/climate_monitor/'