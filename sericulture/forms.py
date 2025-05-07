from django import forms
from .models import MulberryFarm

class MulberryFarmForm(forms.ModelForm):
    class Meta:
        model = MulberryFarm
        fields = ['farmer', 'location', 'size']

from .models import SilkwormBatch

class SilkwormBatchForm(forms.ModelForm):
    class Meta:
        model = SilkwormBatch
        fields = ['farm', 'breed_type', 'quantity', 'start_date', 'harvest_date']
