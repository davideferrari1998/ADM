from django.utils import timezone
from django.test import TestCase
import datetime

from myblog.models import Articoli, ArticoliForm, Autore

# Create your tests here.
class ArticoliFormTests(TestCase):

    def test_future_pub_date(self):
        future_date = timezone.now() + datetime.timedelta(days=1)
        form = ArticoliForm({'autore':'matteo','titolo':'test','testo':'test','pub_date':future_date})
        self.assertIs(form.instance.valid_date(), False)