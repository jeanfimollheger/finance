from django import forms
from budget.models import Flux

JOBS = (
  ("python", "dev Python"),
  ("django", "dev Django"),
  ("gabarit", "Utilisateur gabarit"),
  ("html", "Utilisateur html"),
  ("css","Utilisateur css"),
)

class SignupForm(forms.Form):
  pseudo = forms.CharField(required=False, max_length=8) 
  email = forms.EmailField()
  password = forms.CharField(min_length=6, widget=forms.PasswordInput())
  cgu_accept = forms.BooleanField(initial=False)
  job = forms.MultipleChoiceField(choices=JOBS, widget=forms.CheckboxSelectMultiple())
  #ChoiceField si interdiction de choix multiple et bien sur pas ce widget forms.CheckboxSelectMultiple()

  def clean_pseudo(self):
    pseudo = self.cleaned_data.get("pseudo")
    if "$" in pseudo :
      raise forms.ValidationError("Pas de $ dans le pseudo")
    return pseudo


class FluxModelForm(forms.ModelForm):
  class Meta:
    model = Flux
    fields = ['budget_or_real', 'year', 'date',
              'category','subcategory','period',
              'amount']
    labels = {'budget_or_real':'Budget ou Réel', 'year':'Année', 
              'category' : 'Catégorie','subcategory' : 'Sous-catégorie','period':'Périodicité',
              'amount':'Montant'}
    widgets = {'date': forms.SelectDateWidget(years=range(2023,2030))}


class CreateFluxForm(forms.ModelForm):
  class Meta:
    model = Flux
    fields = ['budget_or_real', 'year', 'date',
              'category','subcategory','period',
              'amount']
    labels = {'budget_or_real':'Budget ou Réel', 'year':'Année', 
              'category' : 'Catégorie','subcategory' : 'Sous-catégorie','period':'Périodicité',
              'amount':'Montant période'}
    widgets = {'date': forms.SelectDateWidget(years=range(2023,2030))}