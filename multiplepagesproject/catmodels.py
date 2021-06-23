from django.db import connections
from django.db import models

class catdisplay(models.Model):
    catname = models.CharField(max_length=100)
    displayorder = models.IntegerField()
    status = models.IntegerField()
    class Meta:
        db_table = "category"


