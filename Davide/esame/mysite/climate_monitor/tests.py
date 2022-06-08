from email.headerregistry import Address
from django.test import TestCase
from django.utils import timezone
import datetime

# Create your tests here.
from .models import Detection, Sensor

class ModelTests(TestCase):


    def test_valid_detection_temperature(self):

        now = timezone.now()
        s =  Sensor(type='T', address='Via Modena 76', CAP='41123')
        #s.save()
        x = Detection(sensor= s, timestamp= now, value= 300)
        #x.save()
        self.assertIs(x.is_valid(), False)

    def test_valid_detection_PM10(self):

        now = timezone.now()
        s =  Sensor(type='Aria', address='Via Modena 76', CAP='41123')
        #s.save()
        x = Detection(sensor= s, timestamp= now, value= 300)
        #x.save()
        self.assertIs(x.is_valid(), False)

    def test_valid_detection_date(self):
        
        time = timezone.now() + datetime.timedelta(days=30)
        s =  Sensor(type='T', address='Via Modena 76', CAP='41123')
        #s.save()
        x = Detection(sensor= s, timestamp= time, value= 10)
        #x.save()
        self.assertIs(x.is_valid(), False)