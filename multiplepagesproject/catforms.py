from django import forms
from multiplepagesproject.catmodels import catdisplay

class categoryforms(forms.ModelForm):
    class Meta:
        model = catdisplay
        fields = "__all__"