from django import forms
from multiplepagesproject.pgemodels import pgedisplay

class pagesforms(forms.ModelForm):
    class Meta:
        model = pgedisplay
        fields = "__all__"