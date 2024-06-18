from rest_framework import serializers
from .models import Faction, Unit, Battle, BattleFaction


class FactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faction
        fields = "__all__"


class UnitSerializer(serializers.ModelSerializer):
    faction = FactionSerializer(many=False)
    # faction = (serializers.StringRelatedField())
    class Meta:
        model = Unit
        fields = "__all__"


class BattleSerializer(serializers.ModelSerializer):
    # factions = FactionSerializer(many=True)  #

    class Meta:
        model = Battle
        fields = "__all__"


class BattleFactionSerializer(serializers.ModelSerializer):
    #battle = (serializers.StringRelatedField())  
    #faction = (serializers.StringRelatedField())  

    battle = BattleSerializer()
    faction = FactionSerializer()

    class Meta:
        model = BattleFaction
        fields = "__all__"
