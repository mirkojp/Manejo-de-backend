import re
from django import forms
from .models import Faction, Unit, Battle, BattleFaction


def validate_warhammer_date_format(value):
    if not value or not re.match(r"^\d{3}\.M\d{1,2}$", value):
        raise forms.ValidationError(
            "Enter a valid Warhammer 40k date format (e.g., 999.M41 or 999.M42)."
        )


class FactionForm(forms.ModelForm):
    class Meta:
        model = Faction
        fields = ["name", "description"]


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ["faction", "name", "unit_type", "strength", "description"]


class BattleForm(forms.ModelForm):

    date = forms.CharField(
        label="Date:",
        widget=forms.TextInput(attrs={"placeholder": "Example: 999.M41"}),
        validators=[validate_warhammer_date_format])

    class Meta:
        model = Battle
        fields = ["name", "date"]
        # fields = ["name", "date", "factions"]
        # widgets = {"factions": forms.CheckboxSelectMultiple(),}


class BattleFactionForm(forms.ModelForm):
    class Meta:
        model = BattleFaction
        fields = ["battle", "faction", "outcome"]
