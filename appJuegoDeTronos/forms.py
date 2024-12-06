from django import forms
from .models import Character, Season


class CharacterForm(forms.ModelForm):
    seasons = forms.ModelMultipleChoiceField(
        queryset=Season.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Character
        fields = ['name', 'description', 'house', 'image', 'seasons']
