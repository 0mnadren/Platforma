from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

from .forms import ProfilForm
from .models import Oblast
from account.models import accepted_check
from administrator.models import Obavestenje
from datetime import datetime


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
                request, 'Vasa prijava je poslata na razmatranje!')
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
    user = request.user
    default_datum = datetime.today()
    obavestenja = Obavestenje.objects.filter(
        profil=user.profil
    ).order_by('-id')

    if request.method == 'POST':
        form = ProfilForm(request.POST or None, request.FILES,
                          instance=request.user.profil)
        if form.is_valid():
            form.save()
            messages.success(request, f'Vas nalog je azuriran!')
            return redirect('profil:profil')
    else:
        form = ProfilForm(instance=request.user.profil)

    context = {
        'obavestenja': obavestenja,
        'form': form,
        'default_datum': default_datum
    }

    return render(request, 'profil/profil.html', context)
