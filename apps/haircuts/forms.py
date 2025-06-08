from django import forms
from apps.haircuts.models import HairCut

        
class HairCutForm(forms.ModelForm):
    
    class Meta:
        model = HairCut
        fields = "__all__"
        