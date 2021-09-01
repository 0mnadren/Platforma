import datetime

from django.contrib import messages
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.http.response import HttpResponse
from django.template.loader import render_to_string

from administrator.validators import superuser_check
from account.models import accepted_check
from profil.models import Profil, Oblast
from .models import Rad, ProsledjenRad
from .forms import RadForm
from programski_pozivi.forms import ProgramskiPozivOdgovoriForm, ProgramskiPozivPitanjaForm
from programski_pozivi.models import ProgramskiPozivOdgovori, ProgramskiPozivPitanja


### ADMIN DEO ###
@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def radovi_admin_home(request):
    return render(request, 'radovi/radovi_admin_home.html')


@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def kreiraj_rad(request):
    if request.method == 'POST':
        form = RadForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            print(form)
            oblasti = form.cleaned_data.get('oblasti')
            for oblast in oblasti:
                oblast_obj = Oblast.objects.get(naziv=oblast)
                obj.oblasti.add(oblast_obj)

            messages.success(request, 'Uspesno ste kreirali naucni rad!')
            return redirect('radovi:radovi_admin_home')
    else:
        form = RadForm()

    context = {
        'form': form
    }

    return render(request, 'radovi/kreiraj_rad.html', context)


@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def lista_radova_admin(request):
    radovi = Rad.objects.all().order_by('programski_poziv')

    return render(request, 'radovi/lista_radova_admin.html', {'radovi': radovi})


@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def naucni_rad_admin(request, pk):
    rad = get_object_or_404(Rad, pk=pk)
    profili = Profil.objects.filter(
        user__profile_accepted=True
    ).filter(
        ~Q(prosledjenrad__rad_id=rad.id)
    )

    # Mozda je potrebno ubaciti jos jedan BoolField u ProsledjenRad "poslat_rad"??
    # filter(Q(prosledjenrad__poslat_rad=False) | Q(prosledjenrad__poslat_rad=None))

    if request.POST:
        korisnici = request.POST.getlist('profili[]')
        for id in korisnici:
            profil = Profil.objects.get(id=id)
            if rad in profil.rad_set.all():
                print('Ne radi nista, profil ima vec taj rad')
            else:
                prosledjen_rad = ProsledjenRad(
                    profil=profil,
                    rad=rad,
                )
                prosledjen_rad.save()
        return redirect('radovi:lista_radova_admin')

    context = {
        'rad': rad,
        'profili': profili,
    }

    return render(request, 'radovi/naucni_rad_admin.html', context)


@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def prosledjeni_radovi_admin(request):
    ime_rada = request.POST.get('ime_rada')
    broj_dana = request.POST.get('broj_dana')

    if ime_rada:
        prosledjeni_radovi = ProsledjenRad.objects.filter(rad__naziv__icontains=ime_rada).order_by('rad')
    elif broj_dana:
        prosledjeni_radovi_dani = ProsledjenRad.objects.filter(
            kada_poslat__lte=datetime.datetime.now() - datetime.timedelta(broj_dana)
        ).filter(zakljucani_odgovori=False)
    else:
        prosledjeni_radovi = ProsledjenRad.objects.all().order_by('rad')
        prosledjeni_radovi_dani = None

    context = {
        'prosledjeni_radovi': prosledjeni_radovi,
        'prosledjeni_radovi_dani': prosledjeni_radovi_dani
    }
    return render(request, 'radovi/prosledjeni_radovi_admin.html', context)


def ime_rada_pretraga(request):

    if request.method == 'POST':
        ime_rada = request.POST.get('ime_rada')
        prosledjeni_radovi = ProsledjenRad.objects.filter(rad__naziv__icontains=ime_rada).order_by('rad')
        context = {
            'prosledjeni_radovi': prosledjeni_radovi
        }

        result = render_to_string('radovi/ime_rada_pretraga.html', context, request)
        return HttpResponse(result)


def recenzije_dani_pretraga(request):

    if request.method == 'POST':
        try:
            broj_dana = int(request.POST.get('broj_dana'))
        except ValueError as e:
            print('Error je ', e)
        prosledjeni_radovi_dani = ProsledjenRad.objects.filter(
            kada_poslat__lte=datetime.datetime.now()-datetime.timedelta(broj_dana)
        ).filter(zakljucani_odgovori=False)
        print(prosledjeni_radovi_dani)
        context = {
            'prosledjeni_radovi_dani': prosledjeni_radovi_dani
        }
        result = render_to_string('radovi/recenzije_dani_pretraga.html', context, request)
        return HttpResponse(result)



@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def oduzimanje_rada_admin(request, pk):
    prosledjen_rad = get_object_or_404(ProsledjenRad, pk=pk)
    if request.POST:
        prosledjen_rad.delete()
        return redirect('radovi:prosledjeni_radovi_admin')


@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def konacna_odluka_rad_admin(request, pk):
    rad = get_object_or_404(Rad, pk=pk)

    if request.method == 'POST' and 'prihvati' in request.POST:
        rad.prihvacen_rad = True
        rad.save()
        return redirect('radovi:radovi_admin_home')
    elif request.method == 'POST' and 'odbij' in request.POST:
        rad.prihvacen_rad = False
        rad.save()
        return redirect('radovi:radovi_admin_home')
    else:
        return redirect('radovi:radovi_admin_home')


### PROFIL DEO ###
@login_required()
@user_passes_test(accepted_check, login_url='account:home', redirect_field_name=None)
def lista_radova_profil(request):
    user = request.user
    radovi = ProsledjenRad.objects.filter(profil=user.profil).filter(zakljucani_odgovori=False)

    print(len(radovi))  # Moze da se iskoristi kao notifikacija na profilu za radove
    broj_radova = len(radovi)

    context = {
        'radovi': radovi,
        'broj_radova': broj_radova,
    }

    return render(request, 'radovi/lista_radova_profil.html', context)


@login_required()
@user_passes_test(accepted_check, login_url='account:home', redirect_field_name=None)
def naucni_rad_profil(request, pk):
    rad = get_object_or_404(Rad, pk=pk)
    pitanja = rad.programski_poziv.programskipozivpitanja
    user = request.user

    odgovori = ProgramskiPozivOdgovori.objects.filter(programski_poziv_pitanja_id=pitanja.id).filter(profil_id=user.profil.id).first()

    prosledjen_rad = ProsledjenRad.objects.filter(profil=user.profil, rad=rad).first()

    if request.method == 'POST' and 'sacuvaj' in request.POST:
        form = ProgramskiPozivOdgovoriForm(request.POST, instance=odgovori)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.programski_poziv_pitanja_id = pitanja.id
            obj.profil_id = user.profil.id
            obj.izracunaj_ukupan_broj_poena()
            obj.save()
            messages.success(request, f'Napravili ste pitanja!')
            return redirect('radovi:lista_radova_profil')
    elif request.method == 'POST' and 'zakljucaj' in request.POST:
        form = ProgramskiPozivOdgovoriForm(request.POST, instance=odgovori)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.programski_poziv_pitanja_id = pitanja.id
            obj.profil_id = user.profil.id
            obj.izracunaj_ukupan_broj_poena()
            obj.save()
            messages.success(request, f'Napravili ste pitanja!')

            prosledjen_rad.zakljucani_odgovori = True
            prosledjen_rad.save()
            return redirect('radovi:lista_radova_profil')
    else:
        form = ProgramskiPozivOdgovoriForm(instance=odgovori)

    # zipuju se pitanja i form(odgovori) da bi mogli zajedno da ih pokazemo
    lista_pitanja = ProgramskiPozivPitanjaForm(data=model_to_dict(ProgramskiPozivPitanja.objects.get(pk=pitanja.id)))
    pitanja_odgovori = zip(lista_pitanja, form)

    context = {
        'rad': rad,
        'pitanja_odgovori': pitanja_odgovori,
        'prosledjen_rad': prosledjen_rad,
        'form': form,
    }

    return render(request, 'radovi/naucni_rad_profil.html', context)
