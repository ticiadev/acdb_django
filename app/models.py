from django.db import models

# Create your models here.
class villager(models.Model):
    name = models.CharField(max_length=12)
    species = models.CharField(max_length=12)
    birthday_month = models.IntegerField()
    birthday_day = models.IntegerField()

    def __str__(self):
        return self.name