from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Faction, Unit, Battle, BattleFaction

admin.site.register(Faction)
admin.site.register(Unit)
admin.site.register(Battle)
admin.site.register(BattleFaction)
