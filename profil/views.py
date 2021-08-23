from django.forms import modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

from .forms import ProfilForm
from .models import Oblast, Profil
from account.models import accepted_check
from administrator.models import Rad, ProsledjenRad, ProgramskiPozivOdgovor, ProgramskiPozivPitanje
from administrator.forms import ProgramskiPozivOdgovorForm


# Ovo je komentar

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

            messages.success(request, 'Vasa prijava je poslata na razmatranje!')
            return redirect('account:status')
        else:
            print("ERROR : Form is invalid")
            print(form.errors)
    else:
        form = ProfilForm()

    return render(request, 'profil/prijava.html', {'form': form})


@login_required()
@user_passes_test(accepted_check, login_url='account:home', redirect_field_name=None)
def profil(request):
    if request.method == 'POST':
        form = ProfilForm(request.POST, request.FILES, instance=request.user.profil)

        if form.is_valid():
            form.save()
            messages.success(request, f'Vas nalog je azuriran!')
            return redirect('profil:profil')
    else:
        form = ProfilForm(instance=request.user.profil)

    return render(request, 'profil/profil.html', {'form': form})


@login_required()
@user_passes_test(accepted_check, login_url='account:home', redirect_field_name=None)
def lista_radova(request):
    user = request.user
    radovi = ProsledjenRad.objects.filter(profil=user.profil)
    return render(request, 'profil/lista_radova.html', {'radovi': radovi})


@login_required()
@user_passes_test(accepted_check, login_url='account:home', redirect_field_name=None)
def naucni_rad_test(request, pk):
    rad = get_object_or_404(Rad, pk=pk)
    print(rad.programski_poziv.programskipozivpitanje_set.all())
    queryset = ProgramskiPozivOdgovor.objects.filter()

    ProgramskiPozivOdgovorSet = modelformset_factory(
        ProgramskiPozivOdgovor,
        fields=('odgovor',),
        )
    if request.method == 'POST':
        formset = ProgramskiPozivOdgovorSet(
            data=request.POST,
            queryset=queryset,
        )

        if formset.is_valid():
            objs = formset.save(commit=False)
            for obj in objs:
                obj.programski_poziv_id = rad.programski_poziv.id
                obj.save()
            messages.success(request, f'Snimili ste odgovore!')
            return redirect('profil:lista_radova')
    else:
        formset = ProgramskiPozivOdgovorSet(queryset=queryset)

    context = {
        'rad': rad,
        'formset': formset
    }
    return render(request, 'profil/naucni_rad_test.html', context)


@login_required()
@user_passes_test(accepted_check, login_url='account:home', redirect_field_name=None)
def naucni_rad(request, pk):
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
            return redirect('profil:lista_radova')
    else:
        form = ProgramskiPozivOdgovorForm()

    context = {
        'rad': rad,
        'form': form
    }
    return render(request, 'profil/naucni_rad.html', context)
