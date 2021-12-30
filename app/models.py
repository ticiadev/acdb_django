from django.db import models


# Create your models here.
class Personality(models.Model):
    type = models.CharField(max_length=12, unique=True)
    gender = models.CharField(max_length=8)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "personalities"

class Villager(models.Model):
    SUBTYPE_CHOICES = [("A", "A"), ("B", "B")]
    name = models.CharField(max_length=12, unique=True)
    species = models.CharField(max_length=12)
    birthday_month = models.IntegerField()
    birthday_day = models.IntegerField()
    catchphrase = models.CharField(max_length=16, blank=True)
    hobby = models.CharField(max_length=12, blank=True)
    fav_color = models.CharField(max_length=12, blank=True)
    fav_song = models.CharField(max_length=12, blank=True)
    is_sanrio = models.BooleanField(blank=True, null=True)
    subtype = models.CharField(max_length=1, choices=SUBTYPE_CHOICES,
                               blank=True)
    # personality_id = models.ForeignKey(Personality,
    #                                    on_delete=models.CASCADE)

    def __str__(self):
        return self.name
