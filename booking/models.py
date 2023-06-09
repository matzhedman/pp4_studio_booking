from django.db import models

# Create your models here.


class Record(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class Offer(models.Model):
    expiration_date = models.DateField(null=True)
