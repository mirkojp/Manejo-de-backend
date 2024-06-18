from django.urls import path
from warhammer_api import views


urlpatterns = [
    path("", views.index_view, name="index"),

    path("factions_rest/", views.factions_rest, name="factions_rest"),
    path("units_rest/", views.units_rest, name="units_rest"),
    path("battle_factions_rest/", views.battle_factions_rest, name="battle_factions_rest"),
    path("battles_rest/", views.battles_rest, name="battles_rest"),
    
    # DEPRECATED REPLACED WITH NEW
    # path("create_faction/", views.create_faction_view, name="create_faction"),
    # path("create_unit", views.create_unit_view, name="create_unit"),
    # path("create_battle_faction/",views.create_battle_faction_view,name="create_battle_faction",),
    # path("create_battle/", views.create_battle_view, name="create_battle"),

    path("new_battle_faction/",views.NewBattleFactionView.as_view(),name="new_battle_faction",),
    path("new_battle/", views.NewBattleView.as_view(), name="new_battle"),
    path("new_faction/", views.NewFactionView.as_view(), name="new_faction"),
    path("new_unit/", views.NewUnitView.as_view(), name="new_unit"),

    path("factions/", views.FactionListView.as_view(), name="faction_list"),
    path("units/", views.UnitListView.as_view(), name="unit_list"),
    path("battles/", views.BattleListView.as_view(), name="battle_list"),
]
