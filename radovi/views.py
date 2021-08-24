from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404

from administrator.validators import superuser_check
from account.models import accepted_check
from profil.models import Profil
from .models import Rad, ProsledjenRad
from programski_pozivi.forms import ProgramskiPozivForm, ProgramskiPozivOdgovorForm
from programski_pozivi.models import ProgramskiPozivPitanje


### ADMIN DEO ###
@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def lista_radova_admin(request):
    radovi = Rad.objects.all()

    return render(request, 'radovi/lista_radova_admin.html', {'radovi': radovi})


@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def naucni_rad_admin(request, pk):
    rad = get_object_or_404(Rad, pk=pk)
    profili = Profil.objects.filter(user__profile_accepted=True)
    form = ProgramskiPozivForm()

    if request.POST:
        korisnici = request.POST.getlist('profili[]')
        for id in korisnici:
            profil = Profil.objects.get(id=id)
            if rad in profil.rad_set.all():
                print('Ne radi nista, profil ima vec taj rad')
            else:
                prosledjen_rad = ProsledjenRad(
                    profil=profil,
                    rad=rad
                )
                prosledjen_rad.save()
        return redirect('radovi:lista_radova_admin')

    context = {
        'rad': rad,
        'form': form,
        'profili': profili,
    }

    return render(request, 'radovi/naucni_rad_admin.html', context)


### PROFIL DEO ###
@login_required()
@user_passes_test(accepted_check, login_url='account:home', redirect_field_name=None)
def lista_radova_profil(request):
    user = request.user
    radovi = ProsledjenRad.objects.filter(profil=user.profil)
    return render(request, 'radovi/lista_radova_profil.html', {'radovi': radovi})


@login_required()
@user_passes_test(accepted_check, login_url='account:home', redirect_field_name=None)
def naucni_rad_profil(request, pk):
    rad = get_object_or_404(Rad, pk=pk)
    user = request.user
    if request.method == 'POST':
        form = ProgramskiPozivOdgovorForm(request.POST)

        if form.is_valid():

            for pitanje in rad.programski_poziv.programskipozivpitanje_set.all():
                obj = form.save(commit=False)
                obj.save()
                pitanje_obj = ProgramskiPozivPitanje.objects.get(pitanje=pitanje)
                obj.pitanje.add(pitanje_obj)
                print(pitanje_obj)
                profil_obj = Profil.objects.get(user=user)
                obj.profil.add(profil_obj)
                print(profil_obj)

            messages.success(request, f'Snimili ste odgovore!')
            return redirect('radovi:lista_radova_profil')
    else:
        form = ProgramskiPozivOdgovorForm()

    context = {
        'rad': rad,
        'form': form
    }
    return render(request, 'radovi/naucni_rad_profil.html', context)
