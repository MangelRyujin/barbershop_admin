from django import forms
from apps.haircuts.models import HairCut,Gallery

        
class HairCutForm(forms.ModelForm):
    
    class Meta:
        model = HairCut
        fields = "__all__"
        
        
class GalleryForm(forms.ModelForm):
    
    class Meta:
        model = Gallery
        fields = "__all__"
        