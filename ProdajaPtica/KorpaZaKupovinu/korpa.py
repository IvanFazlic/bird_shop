from decimal import Decimal
from django.conf import settings
from SalonPtica.models import Ptica

class Korpa(object):
    def __init__(self, request):
        self.sesija = request.session  # tekuca sesija
        korpa = self.sesija.get(settings.KORPA_ZA_KUPOVINU_SESSION_KEY)
        # uzeti korpu iz tekuce sesije, ako je nema kreirati je
        if not korpa:
            korpa = self.sesija[settings.KORPA_ZA_KUPOVINU_SESSION_KEY] = {}
        self.korpa = korpa

    def __iter__(self):
        ptice_ids = self.korpa.keys()
        ptice = Ptica.objects.filter(id__in=ptice_ids)
        korpakopija = self.korpa.copy()
        for ptica in ptice:
            korpakopija[str(ptica.id)]['ptica'] = ptica
        for stavka in korpakopija.values():
            stavka['cena'] = Decimal(stavka['cena'])
            stavka['ukupna_cena'] = stavka['cena'] * stavka['kolicina']
            yield stavka  

    def __len__(self): 
        return sum(stavka['kolicina'] for stavka in self.korpa.values())

    def Dodaj(self, ptica, kolicina=1, dodati_na_kolicinu=True):
        ptica_id = str(ptica.id)
        if ptica_id not in self.korpa:
            self.korpa[ptica_id] = {'kolicina': 0, 'cena': str(ptica.cena)}
        if dodati_na_kolicinu:
            self.korpa[ptica_id]['kolicina'] += kolicina
        else:
            self.korpa[ptica_id]['kolicina'] = kolicina
        self.sesija.modified = True 

    def Ukloni(self, ptica):  
        ptica_id = str(ptica.id)
        if ptica_id in self.korpa:
            del self.korpa[ptica_id]
            self.sesija.modified = True

    def ObrisiJeIzSesije(self):  
        del self.sesija[settings.KORPA_ZA_KUPOVINU_SESSION_KEY]
        self.sesija.modified = True

    def UzmiUkupnuCenu(self):  
        return sum(Decimal(stavka['cena']) * stavka['kolicina'] for stavka in self.korpa.values())
