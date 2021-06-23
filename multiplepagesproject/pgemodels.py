from django.db import connections
from django.db import models

class pgedisplay(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    displayorder = models.IntegerField()
    status = models.IntegerField()
    class Meta:
        db_table = "pages"