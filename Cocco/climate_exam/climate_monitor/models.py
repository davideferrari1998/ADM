from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class SensorTypes(models.TextChoices):
        TEMPERATURA = 'Temperatura',
        PM10 = 'PM10'

class Sensori(models.Model):

    type = models.CharField(choices=SensorTypes.choices, default=SensorTypes.TEMPERATURA, max_length=20)
    indirizzo = models.CharField(max_length=30)
    cap = models.IntegerField(help_text="5 numeri")

    def __str__(self):
        return str(self.pk)


class Rilevamenti(models.Model):
    
    sensore = models.ForeignKey(Sensori, on_delete=models.CASCADE)
    type = models.CharField(choices=SensorTypes.choices, default=SensorTypes.TEMPERATURA, max_length=20)
    timestamp = models.DateTimeField()
    valore = models.FloatField()

    def __str__(self):
         return str(self.pk)

    def is_valid(self):
        actual_ts = timezone.now()

        if self.timestamp > actual_ts:
            return False

        print("check date ok")
    
        if self.type != self.sensore.type:
            print("check type false")
            return False

        if self.type == SensorTypes.TEMPERATURA:
            if self.valore < -80 and self.valore > 80:
                return False
        else:
            if self.valore <= 0 and self.valore > 10:
                return False

        return True