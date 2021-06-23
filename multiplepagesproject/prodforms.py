from django import forms
from multiplepagesproject.prodmodels import proddisplay

class productforms(forms.ModelForm):
    class Meta:
        model = proddisplay
        fields = "__all__"