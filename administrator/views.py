from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404
from django.forms.models import modelformset_factory

from .validators import superuser_check
from profil.models import Profil
from administrator.models import ProgramskiPoziv, ProgramskiPozivPitanje, Rad, ProsledjenRad
from .forms import ProgramskiPozivForm, ProgramskiPozivOdgovorForm


@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def profil(request):
    return render(request, 'administrator/admin_profil.html')


@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def pregled_prijava(request):
    prijave = Profil.objects.all()
    context = {
        'prijave': prijave
    }
    return render(request, 'administrator/pregled_prijava.html', context)


@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def prijava_detaljno(request, pk):

    prijava = get_object_or_404(Profil, pk=pk)
    prijava.pregleda_se = True
    prijava.save()
    context = {
        'prijava': prijava,
    }
    return render(request, 'administrator/prijava_detaljno.html', context)


@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def prijava_prihvacena(request, pk):

    prijava = get_object_or_404(Profil, pk=pk)
    user = prijava.user
    user.profile_accepted = True
    user.save()

    return redirect('administrator:prijave')


@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def prijava_odbijena(request, pk):

    prijava = get_object_or_404(Profil, pk=pk)
    user = prijava.user
    user.profile_accepted = False
    user.save()

    return redirect('administrator:prijave')


@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def kreiraj_programski_poziv(request):
    if request.method == 'POST':
        form = ProgramskiPozivForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f'Napravili ste programski poziv!')
            return redirect('administrator:kreiranje_poziva')
    else:
        form = ProgramskiPozivForm()

    pozivi = ProgramskiPoziv.objects.all()

    context = {
        'form': form,
        'pozivi': pozivi
    }

    return render(request, 'administrator/kreiraj_programski_poziv.html', context)


@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def kreiraj_pitanja_programski_poziv(request, pk):
    programski_poziv = get_object_or_404(ProgramskiPoziv, pk=pk)

    queryset = ProgramskiPozivPitanje.objects.filter(programski_poziv=programski_poziv.id)

    ProgramskiPozivPitanjeSet = modelformset_factory(
        ProgramskiPozivPitanje,
        fields=('pitanje',),
        max_num=10,
        extra=10,
    )
    if request.method == 'POST':
        formset = ProgramskiPozivPitanjeSet(
            data=request.POST,
            queryset=queryset,
        )

        if formset.is_valid():
            objs = formset.save(commit=False)
            for obj in objs:
                obj.programski_poziv_id = programski_poziv.id
                obj.save()
            messages.success(request, f'Napravili ste pitanja!')
            return redirect('administrator:kreiranje_poziva')
    else:
        formset = ProgramskiPozivPitanjeSet(queryset=queryset)

    context = {
        'programski_poziv': programski_poziv,
        'formset': formset,
    }

    return render(request, 'administrator/kreiraj_pitanja.html', context)


@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def lista_naucnih_radova(request):
    radovi = Rad.objects.all()

    return render(request, 'administrator/lista_radova.html', {'radovi': radovi})


@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def naucni_rad(request, pk):
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
        return redirect('administrator:naucni_radovi')

    context = {
        'rad': rad,
        'form': form,
        'profili': profili,
    }

    return render(request, 'administrator/rad.html', context)


