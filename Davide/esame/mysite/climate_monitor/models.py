from django.db import models
from django.utils import timezone

# Create your models here.

class Sensor(models.Model):
    sensors = (('T', 'Temperature'),('Aria', 'PM10'))
    type = models.CharField(max_length=15, choices=sensors)
    address = models.CharField(max_length=50)
    CAP = models.CharField(max_length=6)

    def __str__(self):
        return str(self.type)
    

class Detection(models.Model):
    
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    timestamp = models.DateTimeField('Timestamp')
    value = models.IntegerField()

    def __str__(self):
        return str(self.timestamp)

    def is_valid(self):
        
        now = timezone.now()
        if self.timestamp <= now:
            if self.sensor.type == 'T':
                if -30 <= self.value <= 60:
                    return True
                else:
                    return False
            else:
                #Caso Di PM10
                if 0 <= self.value <= 10:
                    return True
                else:
                    return False
        else:
            return False
        
"""
class TempSensor(models.Model):

    sensor = models.OneToOneField(Sensor)
    type = 'Temperature'

class AriaSensor(models.Model):
    sensor = models.OneToOneField(Sensor)
    type = 'PM10'
"""

"""
class TypeSensor(models.Model):

    s = (('T', 'Temperature'),('Aria', 'PM10'))
    name = models.CharField(max_length=15, choices=s)
    
    def __str__(self):
        return str(self.name)
"""