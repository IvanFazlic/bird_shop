from django.shortcuts import render, get_object_or_404
from .models import Segment, Ptica

def ListaPtica(request, segment_slug=None):
    segment = None
    segmenti = Segment.objects.all()
    ptice = Ptica.objects.filter(raspoloziv=True)

    if segment_slug:
        segment = get_object_or_404(Segment, slug=segment_slug)
        ptice = ptice.filter(segment=segment)

    return render(request, 'SalonPtica/ptica/list.html', {'segment': segment, 'segmenti': segmenti, 'ptice': ptice})

def DetaljiPtica(request, id, slug):
    ptica = get_object_or_404(Ptica, id=id, slug=slug, raspoloziv=True)
    return render(request, 'SalonPtica/ptica/detail.html', {'ptica': ptica})
