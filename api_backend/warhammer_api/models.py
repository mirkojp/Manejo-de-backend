

# Create your models here.

from django.db import models


class Faction(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Unit(models.Model):
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE, related_name="units")
    name = models.CharField(max_length=100)
    unit_type = models.CharField(max_length=100)  # e.g., Infantry, Cavalry, Artillery
    strength = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.faction.name})"

class Battle(models.Model):
    name = models.CharField(max_length=100)
    date = models.CharField(max_length=10) # example 999.M41,
    # factions = models.ManyToManyField(Faction, through="BattleFaction")

    def __str__(self):
        return self.name

class BattleFaction(models.Model):
    battle = models.ForeignKey(Battle, on_delete=models.CASCADE)
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE)
    outcome = models.CharField(max_length=100, blank=True)  # e.g., Victory, Defeat

    class Meta:
        # Ensure that no duplicate battle-faction pairs can exist
        unique_together = ('battle', 'faction')

    def __str__(self):
        return f"{self.faction.name} in {self.battle.name}"
