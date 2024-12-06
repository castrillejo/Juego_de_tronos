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
        fields = ['name', 'description', 'house', 'image', 'seasons','is_alive']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
