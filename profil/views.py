from re import I
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

from .forms import ProfilForm
from .models import Oblast, Profil
from account.models import accepted_check
from administrator.models import Anketa, Obavestenje
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout
# class PrijavaView(CreateView):
#     model = ProfilForm
#     template_name = 'profil/prijava.html'
#     fields = '__all__'

# Ovo je komentar

@login_required()
def prijava(request):
    if request.method == 'POST':
        form = ProfilForm(request.POST, request.FILES)
        print(request.POST)
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
        form = ProfilForm(request.POST or None, request.FILES, instance=request.user.profil)
        if form.is_valid():
            form.save()
            messages.success(request, f'Vas nalog je azuriran!')
            return redirect('profil:profil')
    else:
        form = ProfilForm(instance=request.user.profil)

    return render(request, 'profil/profil.html', {'form': form})



@login_required()
def obavestenja(request):

    user = request.user

    obavestenja = Obavestenje.objects.filter(
        profil = user.profil
    )

    # print(obavestenja)
    # gde je profil == user.profil
    # print('obavestenja su: ' + str(obavestenja))
    context = {
        'obavestenja': obavestenja
    }

    return render(request, 'profil/obavestenja.html', context)



@login_required()
def ankete(request):

    ankete = Anketa.objects.all()
    context = {
        'ankete': ankete
    }

    return render(request, 'profil/ankete.html', context)