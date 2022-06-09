from django.test import TestCase
from django.utils import timezone
import datetime

# Create your tests here.

from .models import Detection, Sensor

class ModelTests(TestCase):

    def test_valid_detection_temperature(self):

        now = timezone.now()
        s =  Sensor(type='Temperature', address='Via Modena 76', CAP='41123')
        x = Detection(sensor= s, type= s.type, timestamp= now, value= 300)
        self.assertIs(x.is_valid(), False)

    def test_valid_detection_PM10(self):

        now = timezone.now()
        s =  Sensor(type='PM10', address='Via Modena 76', CAP='41123')
        x = Detection(sensor= s, type= s.type, timestamp= now, value= 300)
        self.assertIs(x.is_valid(), False)

    def test_valid_detection_date(self):

        now = timezone.now() + datetime.timedelta(days=30)
        s =  Sensor(type='PM10', address='Via Modena 76', CAP='41123')
        x = Detection(sensor= s, type= s.type, timestamp= now, value= 5)
        self.assertIs(x.is_valid(), False)

    def test_valid_detection_type(self):

        now = timezone.now()
        s =  Sensor(type='Temperature', address='Via Modena 76', CAP='41123')
        x = Detection(sensor= s, type= 'PM10', timestamp= now, value= 5)
        self.assertIs(x.is_valid(), False)

    