from django.contrib import admin
from .models import Villager, Personality, Coffee, Game, Amiibo, House, \
    Furniture

# Register your models here.
admin.site.register(Villager)
admin.site.register(Personality)
admin.site.register(Coffee)
admin.site.register(Game)
admin.site.register(Amiibo)
admin.site.register(House)
admin.site.register(Furniture)
