from django.db import models
from django.utils import timezone
from django.forms import ModelForm
from django.forms import widgets
# Create your models here.

"""
class SensorType(models.Model):
    
    s = (('Temperature', 'Temperature'),('PM10', 'PM10'))
    name = models.CharField(max_length=15, choices=s)
    
    def __str__(self):
        return str(self.name)

"""
class Sensor(models.Model):
    
    s = (('Temperature', 'Temperature'),('PM10', 'PM10'))
    type = models.CharField(max_length=15, choices=s)
    address = models.CharField(max_length=50)
    CAP = models.CharField(max_length=6)

    def __str__(self):
        return str(self.id)

class Detection(models.Model):
    
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    s = (('Temperature', 'Temperature'),('PM10', 'PM10'))
    type = models.CharField(max_length=15, choices=s)
    timestamp = models.DateTimeField('Timestamp')
    value = models.IntegerField()

    def __str__(self):
        return str(self.timestamp)

    def is_valid(self):
        
        #Controllo data nel futuro
        now = timezone.now()
        if self.timestamp > now:
            return False

        #Controllo che il tipo sia uguale
        if self.sensor.type != self.type:
            return False

        #Controllo i valori della detection
        if self.type == 'Temperature':
            if self.value <= -30 or self.value >= 60:
                return False
        else:
            if self.value < 0 or self.value > 10:
                return False
            
        return True

        
class SensorForm(ModelForm):
    class Meta:
        model = Sensor
        fields = '__all__'
