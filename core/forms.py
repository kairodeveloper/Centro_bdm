import django.forms as forms
from django.forms.widgets import ClearableFileInput
from .models import *

class ParticipanteForm(forms.ModelForm):

    class Meta:
        model = Participante
        fields = '__all__'
