from django import forms

IZBOR_BROJA_PTICA = [(i, str(i)) for i in range(1, 11)]

class FormaZaDodavanjePticaUKorpu(forms.Form):
    kolicina = forms.TypedChoiceField(choices=IZBOR_BROJA_PTICA, empty_value=1, coerce=int)  
    dodati_na_kolicinu = forms.BooleanField(required=False, initial=True, widget=forms.HiddenInput)
