from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404
from django.forms.models import modelformset_factory

from administrator.validators import superuser_check
from .models import ProgramskiPoziv, ProgramskiPozivPitanje
from .forms import ProgramskiPozivForm


@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def kreiraj_programski_poziv(request):
    if request.method == 'POST':
        form = ProgramskiPozivForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f'Napravili ste programski poziv!')
            return redirect('programski_pozivi:kreiranje_poziva')
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
            return redirect('programski_pozivi:kreiranje_poziva')
    else:
        formset = ProgramskiPozivPitanjeSet(queryset=queryset)

    context = {
        'programski_poziv': programski_poziv,
        'formset': formset,
    }

    return render(request, 'programski_pozivi/kreiraj_pitanja.html', context)
