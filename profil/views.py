from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.translation import gettext_lazy as _

from .forms import ProfilForm
from .models import Oblast
from account.models import accepted_check
from administrator.models import Obavestenje, Obrisanostanje
from datetime import datetime
from django.db.models import Q
from radovi.models import ProsledjenRad
from ankete.models import AnketaPopunjena
from .validators import my_hash


@login_required()
def prijava(request):
    if request.method == 'POST':
        form = ProfilForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user_id = request.user.id
            obj.save()

            oblasti = form.cleaned_data.get('oblasti')
            for oblast in oblasti:
                oblast_obj = Oblast.objects.get(naziv=oblast)
                obj.oblasti.add(oblast_obj)

            messages.success(
                request, _('Vaša prijava je poslata na razmatranje!'))
            return redirect('account:status')
        else:
            print("ERROR : Form is invalid")
    else:
        form = ProfilForm()

    return render(request, 'profil/prijava.html', {'form': form})


@login_required()
@user_passes_test(accepted_check, login_url='account:home', redirect_field_name=None)
def profil(request):
    user = request.user
    default_datum = datetime.today()
    prosledjeni_radovi = ProsledjenRad.objects.filter(profil=user.profil, zakljucani_odgovori=False)
    nepopunjene_ankete = AnketaPopunjena.objects.filter(profil=user.profil, popunjena_anketa=False)

    obavestenja = Obrisanostanje.objects.filter(profil=user.profil)
    
    if request.method == 'POST':
        form = ProfilForm(request.POST or None, request.FILES,
                          instance=request.user.profil)
        if form.is_valid():
            form.save()
            messages.success(request, _(f'Vaš nalog je ažuriran!'))
            return redirect('profil:profil')
    else:
        form = ProfilForm(instance=request.user.profil)

    context = {
        'obavestenja': obavestenja,
        'form': form,
        'default_datum': default_datum,
        'prosledjeni_radovi': prosledjeni_radovi,
        'nepopunjene_ankete': nepopunjene_ankete
    }

    return render(request, 'profil/profil.html', context)


@login_required()
@user_passes_test(accepted_check, login_url='account:home', redirect_field_name=None)
def obrisi_obavestenje(request, pk):
    obavestenje = get_object_or_404(Obavestenje, pk=pk)

    obavestenje_stanje = get_object_or_404(Obrisanostanje, profil=request.user.profil, obavestenje=obavestenje)
    if request.method == 'GET':
        obavestenje_stanje.delete()

    return redirect('profil:profil')



#ukloniti, i ukloniti URL
@login_required()
@user_passes_test(accepted_check, login_url='account:home', redirect_field_name=None)
def search(request):
    user = request.user
    results = []
    if request.method == "GET":
        query = request.GET.get('search')
        if query == '':
            query = my_hash() # na ovaj nacin sam resio da ne prikazuje pri unosenju nicega sve rezultate ( it's a fun way :D )
            print(query)
        results = Obrisanostanje.objects.filter(profil=user.profil).filter(Q(obavestenje__naslov__icontains=query) | Q(obavestenje__tekst__icontains=query))# | Q(datum_vreme_kreiranja__icontains=query) )
        
        # for res in results:
        #     print(res)
    return render(request, 'profil/search.html', {'query': query, 'results': results})


@login_required()
@user_passes_test(accepted_check, login_url='account:home', redirect_field_name=None)
def obavestenje_detaljno(request, pk):
    obavestenje = get_object_or_404(Obavestenje, pk=pk)
    obavestenje_stanje = get_object_or_404(Obrisanostanje, profil=request.user.profil, obavestenje=obavestenje)
    
    if obavestenje_stanje:
        context = {
            'obavestenje': obavestenje,
        }
        return render(request, 'profil/obavestenje_detaljno.html', context)
    else:
        return redirect('profil:profil')
