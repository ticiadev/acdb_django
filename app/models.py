from django.db import models


# Create your models here.
class Personality(models.Model):
    type = models.CharField(max_length=12, unique=True)
    gender = models.CharField(max_length=8)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name_plural = "personalities"

class Coffee(models.Model):
    beans = models.CharField(max_length=20)
    milk = models.CharField(max_length=8)
    sugar = models.IntegerField()

    def __str__(self):
        return self.id

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
    # personality = models.ForeignKey(Personality,
    #                                    on_delete=models.CASCADE)
    # coffee_id = models.ForeignKey(Coffee, on_delete=models.SET_NULL,
    # blank=True, null=True)

    def __str__(self):
        return self.name

class Amiibo(models.Model):
    series = models.CharField(max_length=20, unique=True)
    card_id = models.IntegerField()
    acquired = models.BooleanField(blank=True, null=True)
    # villager = models.OneToOneField(Villager)

    def __str__(self):
        return self.id

class Game(models.Model):
    name = models.CharField(max_length=20, unique=True)
    console = models.CharField(max_length=12)
    year_released = models.IntegerField()
    # villagers = models.ManyToManyField(Villager)

    def __str__(self):
        return self.name

class House(models.Model):
    wallpaper = models.CharField(max_length=16)
    floor = models.CharField(max_length=16)
    music = models.CharField(max_length=16, blank=True)
    # game = models.ForeignKey(Game, on_delete=models.CASCADE)
    # villager = models.ForeignKey(Villager, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

class Furniture(models.Model):
    name = models.CharField(max_length=20, unique=True)
    buy_price = models.IntegerField()
    sell_price = models.IntegerField()
    style = models.CharField(max_length=20, blank=True)
    on_surface = models.BooleanField(blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    # house_id = models.ManytoManyField(House)

    def __str__(self):
        return self.name
