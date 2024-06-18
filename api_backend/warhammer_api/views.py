# Create your views here.
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.views.generic import ListView,CreateView
from .forms import FactionForm,BattleForm,BattleFactionForm,UnitForm
from .models import Faction,Unit,Battle,BattleFaction
from .serializers import FactionSerializer,UnitSerializer,BattleSerializer,BattleFactionSerializer




def index_view(request):
    return render(request, "index.html")


def get_all_factions():
    factions = Faction.objects.all().order_by("name")
    factions_serializers = FactionSerializer(factions, many=True)
    return factions_serializers.data


def factions_rest(request):
    factions = get_all_factions()
    return JsonResponse(factions, safe=False)

# DEPRECATED REPLACED WITH NewFactinView
# def create_faction_view(request):
#     if request.method == "POST":
#         faction_form = FactionForm(request.POST)
#         if faction_form.is_valid():
#             faction_form.save()
#             return HttpResponseRedirect("/")
#     if request.method == "GET":
#         faction_form = FactionForm()
#         csrf_token = get_token(request)
#         html_form = f"""
#             <form method="post">
#                 <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
#                 {faction_form.as_p()}
#                 <button type="submit">Submit</button>
#             </form>
#         """
#         return HttpResponse(html_form)


class NewFactionView(CreateView):
    form_class = FactionForm
    template_name = "faction_form.html" 
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["csrf_token"] = get_token(self.request)
        return context


def get_all_units():
    units = Unit.objects.all().order_by("name")
    units_serializers = UnitSerializer(units, many=True)
    return units_serializers.data


def units_rest(request):
    units = get_all_units()
    return JsonResponse(units, safe=False)

# DEPRECATED REPLACED WITH NewUnitView
# def create_unit_view(request):
#     if request.method == "POST":
#         unit_form = UnitForm(request.POST)
#         if unit_form.is_valid():
#             unit_form.save()
#             return HttpResponseRedirect("/")
#     if request.method == "GET":
#         unit_form = UnitForm()
#         csrf_token = get_token(request)
#         html_form = f"""
#             <form method="post">
#                 <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
#                 {unit_form.as_p()}
#                 <button type="submit">Submit</button>
#             </form>
#         """
#         return HttpResponse(html_form)


class NewUnitView(CreateView):
    form_class = UnitForm
    template_name = "unit_form.html" 
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["csrf_token"] = get_token(self.request)
        return context


def get_all_battles():
    battles = Battle.objects.all().order_by("date")
    battles_serializers = BattleSerializer(battles, many=True)
    return battles_serializers.data


def battles_rest(request):
    battles = get_all_battles()
    return JsonResponse(battles, safe=False)

# DEPRECATED REPLACED WITH NewBattleView
# def create_battle_view(request):
#     if request.method == "POST":
#         battle_form = BattleForm(request.POST)
#         if battle_form.is_valid():
#             battle_form.save()
#             return HttpResponseRedirect("/")
#     if request.method == "GET":
#         battle_form = BattleForm()
#         csrf_token = get_token(request)
#         html_form = f"""
#             <form method="post">
#                 <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
#                 {battle_form.as_p()}
#                 <button type="submit">Submit</button>
#             </form>
#         """
#         return HttpResponse(html_form)


class NewBattleView(CreateView):
    form_class = BattleForm
    template_name = "battle_form.html" 
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["csrf_token"] = get_token(self.request)
        return context


def get_all_battle_factions():
    battle_factions = BattleFaction.objects.all()
    battle_factions_serializers = BattleFactionSerializer(battle_factions, many=True)
    return battle_factions_serializers.data


def battle_factions_rest(request):
    battle_factions = get_all_battle_factions()
    return JsonResponse(battle_factions, safe=False)
# DEPRECATED REPLACED WITH NewBattleFactionView
# def create_battle_faction_view(request):
#     if request.method == "POST":
#         battle_faction_form = BattleFactionForm(request.POST)
#         if battle_faction_form.is_valid():
#             battle_faction_form.save()
#             return HttpResponseRedirect("/")
#         else:
#             # For some reason, when its duplicated it returned null, HttpResponseBadRequest
#             # didnt work, little time to think in anything else used this
#             error_message = "This faction already participates in this battle."
#             return render(request, 'error.html', {'message': error_message})

#     if request.method == "GET":
#         battle_faction_form = BattleFactionForm()
#         csrf_token = get_token(request)
#         html_form = f"""
#             <form method="post">
#                 <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
#                 {battle_faction_form.as_p()}
#                 <button type="submit">Submit</button>
#             </form>
#         """
#         return HttpResponse(html_form)

class NewBattleFactionView(CreateView):
    form_class = BattleFactionForm
    template_name = "battle_faction_form.html" 
    success_url = "/"  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["csrf_token"] = get_token(self.request)
        return context


class FactionListView(ListView):
    model = Faction
    template_name = "factions.html"
    context_object_name = "factions"


class UnitListView(ListView):
    model = Unit
    template_name = "units.html"
    context_object_name = "units"

class BattleListView(ListView):
    model = Battle
    template_name = "battles.html"
    context_object_name = "battles"
