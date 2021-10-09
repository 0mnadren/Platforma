from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _

from administrator.validators import superuser_check
from .models import ProgramskiPoziv, ProgramskiPozivPitanja
from .forms import ProgramskiPozivForm, ProgramskiPozivPitanjaForm


@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def kreiraj_programski_poziv(request):
    if request.method == 'POST':
        form = ProgramskiPozivForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, _(f'Napravili ste programski poziv!'))
            return redirect('programski_pozivi:kreiraj_programski_poziv')
    else:
        form = ProgramskiPozivForm()

    pozivi = ProgramskiPoziv.objects.all()

    context = {
        'form': form,
        'pozivi': pozivi
    }

    return render(request, 'programski_pozivi/kreiraj_programski_poziv.html', context)


@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def detaljno_programski_poziv(request, pk):
    programski_poziv = get_object_or_404(ProgramskiPoziv, pk=pk)
    programski_poziv_pitanja = ProgramskiPozivPitanja.objects.filter(programski_poziv=programski_poziv)

    context = {
        'programski_poziv': programski_poziv,
        'programski_poziv_pitanja': programski_poziv_pitanja
    }

    return render(request, 'programski_pozivi/detaljno_programski_poziv.html', context)


@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def azuriraj_programski_poziv(request, pk):
    programski_poziv = get_object_or_404(ProgramskiPoziv, pk=pk)

    if request.method == "POST":
        form = ProgramskiPozivForm(request.POST, instance=programski_poziv)
        if form.is_valid():

            form.save()
            messages.success(request, _(f'Uspešno ste ažurirali programski poziv!'))
            return redirect('programski_pozivi:kreiraj_programski_poziv')
    else:
        form = ProgramskiPozivForm(instance=programski_poziv)

    context = {
        'form': form,
        'programski_poziv': programski_poziv
    }
    return render(request, 'programski_pozivi/azuriraj_programski_poziv.html', context)


@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def obrisi_programski_poziv(request, pk):
    programski_poziv = get_object_or_404(ProgramskiPoziv, pk=pk)

    if request.method == 'POST':
        programski_poziv.delete()
        return redirect('programski_pozivi:kreiraj_programski_poziv')

    context = {
        'programski_poziv': programski_poziv
    }
    return render(request, 'programski_pozivi/obrisi_programski_poziv.html', context)


### PITANJA ###
@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def kreiraj_pitanja_programski_poziv(request, pk):
    programski_poziv = get_object_or_404(ProgramskiPoziv, pk=pk)

    if request.method == 'POST':
        form = ProgramskiPozivPitanjaForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.programski_poziv_id = programski_poziv.id
            obj.save()
            messages.success(request, _(f'Napravili ste pitanja!'))
            return redirect('programski_pozivi:kreiraj_programski_poziv')
    else:
        form = ProgramskiPozivPitanjaForm()

    context = {
        'form': form,
        'programski_poziv': programski_poziv
    }

    return render(request, 'programski_pozivi/kreiraj_pitanja.html', context)


@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def detaljno_pitanja_programski_poziv(request, pk):
    pitanja = get_object_or_404(ProgramskiPozivPitanja, pk=pk)

    if request.method == "POST":
        form = ProgramskiPozivPitanjaForm(request.POST, instance=pitanja)
        if form.is_valid():

            form.save()
            messages.success(request, _(f'Uspešno ste ažurirali pitanja!'))
            return redirect('programski_pozivi:kreiraj_programski_poziv')
    else:
        form = ProgramskiPozivPitanjaForm(instance=pitanja)

    context = {
        'form': form,
        'pitanja': pitanja
    }
    return render(request, 'programski_pozivi/detaljno_pitanja.html', context)
