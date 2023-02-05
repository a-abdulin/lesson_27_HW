from django.db import models


class ADS(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, default='')
    author = models.CharField(max_length=100, default='')
    price = models.FloatField()
    description = models.CharField(max_length=500, default='')
    address = models.CharField(max_length=250, default='')
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name
class Categories(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, default='')

    def __str__(self):
        return self.name