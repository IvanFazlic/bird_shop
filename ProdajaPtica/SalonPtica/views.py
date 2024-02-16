from django.shortcuts import render, get_object_or_404
from KorpaZaKupovinu.forms import FormaZaDodavanjePticaUKorpu
from .models import Segment, Ptica
from KorpaZaKupovinu.korpa import Korpa

def ListaPtica(request, segment_slug=None):
    segment = None
    segmenti = Segment.objects.all()
    ptice = Ptica.objects.filter(raspoloziv=True)
    
    if segment_slug:
        segment = get_object_or_404(Segment, slug=segment_slug)
        ptice = ptice.filter(segment=segment)
    
    korpa = Korpa(request)
    return render(request, 'SalonPtica/ptica/list.html', {'segment': segment, 'segmenti': segmenti, 'ptice': ptice, 'korpa': korpa})

def DetaljiPtica(request, id, slug):
    ptica = get_object_or_404(Ptica, id=id, slug=slug, raspoloziv=True)
    korpa = Korpa(request)
    formazadodavanjepticaaukorpu = FormaZaDodavanjePticaUKorpu()
    return render(request,'SalonPtica/ptica/detail.html',
                  {'ptica': ptica, 'formazadodavanjepticaukorpu': formazadodavanjepticaaukorpu, 'korpa': korpa})
