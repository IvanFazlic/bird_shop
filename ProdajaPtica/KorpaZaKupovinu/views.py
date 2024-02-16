from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from SalonPtica.models import Ptica
from .korpa import Korpa
from .forms import FormaZaDodavanjePticaUKorpu

@require_POST  # dekorator za prihvatanje POST zahteva
def DodajUKorpu(request, ptica_id):
    korpa = Korpa(request)
    ptica = get_object_or_404(Ptica, id=ptica_id)
    form = FormaZaDodavanjePticaUKorpu(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        korpa.Dodaj(
            ptica=ptica,
            kolicina=cd['kolicina'],
            dodati_na_kolicinu=cd['dodati_na_kolicinu']
        )
    return redirect('KorpaZaKupovinu:DetaljiKorpe')

@require_POST
def UkloniIzKorpe(request, ptica_id):
    korpa = Korpa(request)
    ptica = get_object_or_404(Ptica, id=ptica_id)
    korpa.Ukloni(ptica)
    return redirect('KorpaZaKupovinu:DetaljiKorpe')

def DetaljiKorpe(request):
    korpa = Korpa(request)
    for stavka in korpa:
        stavka['formazaazuriranjekolicine'] = FormaZaDodavanjePticaUKorpu(
            initial={'kolicina': 1, 'dodati_na_kolicinu': True}
        )
    return render(request, 'KorpaZaKupovinu/detail.html', {'korpa': korpa})
