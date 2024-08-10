from django import forms
from .models import Monster, MonsterAttribute, MonsterType

class MonsterSearchForm(forms.Form):
    monster_name = forms.CharField(required=False, label="Monster Name", max_length=100)
    monster_num = forms.IntegerField(required=False, label="Monster Number")
    monster_attributes = forms.MultipleChoiceField(required=False, label="Monster Attribute" ,choices=MonsterAttribute.Attribute.choices, widget=forms.CheckboxSelectMultiple)
    monster_types = forms.MultipleChoiceField(required=False, label="Monster Type", choices=MonsterType.Type.choices, widget=forms.CheckboxSelectMultiple)
    # awakenings = forms.MultipleChoiceField(required=False, label="Monster Awakenings", choices=_, widget=forms.CheckboxSelectMultiple)
    evolutions = forms.BooleanField(required=False, label="Include Evolutions")

    monster_name.widget.attrs.update({"class":"text_search_input"})