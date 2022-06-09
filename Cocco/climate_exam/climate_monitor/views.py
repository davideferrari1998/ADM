from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import Rilevamenti, SensorTypes
from django.http import JsonResponse

# Create your views here.
def letturaView(request, tipo_lettura):
    if tipo_lettura not in SensorTypes.labels:
        return HttpResponseNotFound()
    if tipo_lettura != 'Temperatura':
        tipo_lettura = tipo_lettura.upper()
    queryset = Rilevamenti.objects.filter(type = tipo_lettura)
    #validazione
    valid_elems = []
    sensor_ids = set()
    for elem in queryset:
        if elem.is_valid() == True:
            valid_elems.append(elem)
            sensor_ids.add(elem.sensore_id)
    print(sensor_ids)
    print(valid_elems)
    mean_map = {}

    for id in sensor_ids:
        cont = 0
        total = 0
        for elem in valid_elems:
            if elem.sensore_id == id:
                cont = cont + 1
                total = total + elem.valore
        mean_map[id] = total/cont    

    return render(request, "sensor.html", {'mean_map': mean_map})

def letturaViewJson(request, tipo_lettura):
    if tipo_lettura not in SensorTypes.labels:
        return HttpResponseNotFound()
    if tipo_lettura != 'Temperatura':
        tipo_lettura = tipo_lettura.upper()
    queryset = Rilevamenti.objects.filter(type = tipo_lettura)
    #validazione
    valid_elems = []
    sensor_ids = set()
    for elem in queryset:
        if elem.is_valid() == True:
            valid_elems.append(elem)
            sensor_ids.add(elem.sensore_id)
    print(sensor_ids)
    print(valid_elems)
    mean_map = {}

    for id in sensor_ids:
        cont = 0
        total = 0
        for elem in valid_elems:
            if elem.sensore_id == id:
                cont = cont + 1
                total = total + elem.valore
        mean_map[id] = total/cont    

    return JsonResponse(mean_map)

def sensoriJquery(request):
    print("ok")
    return render(request, "jsonresp.html", {})