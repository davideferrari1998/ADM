from django.forms import ModelForm
from .models import Rilevamenti

class RilevamentoForm(ModelForm):
    class Meta:
        model = Rilevamenti
        fields = '__all__'