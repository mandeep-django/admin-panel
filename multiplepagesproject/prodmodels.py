from django.db import connections
from django.db import models

class proddisplay(models.Model):
    categoryid = models.IntegerField()
    pname = models.CharField(max_length=100)
    pprice = models.IntegerField()
    pcontent = models.TextField(max_length=100)
    pimage = models.FileField()
    pdisplayorder = models.IntegerField()
    pstatus = models.IntegerField()
    class Meta:
        db_table = "product"