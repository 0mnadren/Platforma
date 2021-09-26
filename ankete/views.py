from django.contrib import messages
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404

from account.models import accepted_check
from administrator.validators import superuser_check
from .models import Anketa, AnketaPitanje, AnketaPopunjena
from django.contrib.auth.decorators import login_required, user_passes_test
from . forms import CreateAnketaForm, CreateAnketaPitanjeForm
from profil.models import Oblast, Profil


### ANKETE ADMIN ###
@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def admin_ankete(request):
    ankete = Anketa.objects.all()
    context = {
        'ankete': ankete
    }
    return render(request, 'ankete/admin_ankete.html', context)


@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def create_anketa(request):
    form = CreateAnketaForm()
    if request.method == 'POST':
        form = CreateAnketaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Napravili ste anketu!')
        return redirect('ankete:admin_ankete')
    context = {'form': form}
    return render(request, 'ankete/create_ankete_form.html', context)


@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def delete_anketa(request, pk):
    anketa = get_object_or_404(Anketa, pk=pk)
    if request.method == "POST":
        anketa.delete()
        messages.success(request, f'Uspešno ste izbrisali anketu {anketa}!')
        return redirect('ankete:admin_ankete')
    context = {'item': anketa}
    return render(request, 'ankete/delete_anketa.html', context)


@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def create_pitanje(request, pk):
    form = CreateAnketaPitanjeForm()
    if request.method == 'POST':
        form = CreateAnketaPitanjeForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.anketa_id = pk
            obj.save()
            messages.success(request, f'Napravili ste pitanje!')
        return redirect('ankete:create_pitanje', pk)
    context = {'form': form}
    return render(request, 'ankete/create_pitanje_form.html', context)


@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def posalji_anketa(request, pk):
    anketa = get_object_or_404(Anketa, pk=pk)
    oblasti = Oblast.objects.all()
    profili = Profil.objects.filter(user__profile_accepted=True)

    if anketa.anketapitanje_set.all():
        if request.POST and 'posalji_oblast' in request.POST:
            izabrane_oblasti = request.POST.getlist('oblasti[]')
            if izabrane_oblasti:
                for profil in profili:
                    for oblast_profila in profil.oblasti.all():
                        if oblast_profila.naziv in izabrane_oblasti:
                            profil.save()
                            profil.anketa_set.add(anketa)
                    else:
                        print('Nema takvih profila')
                messages.success(request, f'Poslali ste anketu po oblastima!')
                return redirect('ankete:admin_ankete')
            else:
                messages.success(request, f'Niste izabrali oblast!')
                return redirect('ankete:posalji_anketa', pk=pk)
        elif request.POST and 'posalji_svima' in request.POST:
            for profil in profili:
                profil.save()
                profil.anketa_set.add(anketa)
            messages.success(request, f'Poslali ste anketu svima!')
            return redirect('ankete:admin_ankete')
    else:
        messages.success(request, f'Nije moguće poslati korisnicima, jer niste napravili pitanja za ovu anketu!')
        return redirect('ankete:create_pitanje', pk=pk)

    context = {
        'oblasti': oblasti,
        'anketa': anketa
    }

    return render(request, 'ankete/posalji_anketa_form.html', context)


@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def rezultat_anketa(request, pk):
    anketa = get_object_or_404(Anketa, pk=pk)
    pitanja = AnketaPitanje.objects.filter(anketa_id=pk)
    context = {
        'anketa': anketa,
        'pitanja': pitanja

    }
    return render(request, 'ankete/rezultat_anketa.html', context)


### ANKETE PROFIL ###
@login_required()
@user_passes_test(accepted_check, login_url='account:home', redirect_field_name=None)
def ankete(request):
    user = request.user
    nepopunjene_ankete = AnketaPopunjena.objects.filter(
        profil=user.profil,  popunjena_anketa=False).order_by('-id')
    popunjene_ankete = AnketaPopunjena.objects.filter(
        profil=user.profil,  popunjena_anketa=True).order_by('-id')
    context = {
        'nepopunjene_ankete': nepopunjene_ankete,
        'popunjene_ankete': popunjene_ankete
    }

    return render(request, 'ankete/lista_anketa_profil.html', context)


@login_required()
@user_passes_test(accepted_check, login_url='account:home', redirect_field_name=None)
def glasaj_anketa(request, pk):
    anketa = get_object_or_404(Anketa, pk=pk)
    pitanja = AnketaPitanje.objects.filter(anketa_id=pk)
    anketa_popunjena_stanje = AnketaPopunjena.objects.filter(
        anketa=anketa, profil=request.user.profil, popunjena_anketa=False
    )

    if anketa_popunjena_stanje:
        if request.method == 'POST':
            i = 0
            for pitanje in pitanja:
                i += 1
                opcije = request.POST.getlist(f'pitanje{i}[]')
                for opcija in opcije:
                    if opcija == 'opcija1':
                        pitanje.opcija_one_count += 1
                        pitanje.save()
                    elif opcija == 'opcija2':
                        pitanje.opcija_two_count += 1
                        pitanje.save()
                    elif opcija == 'opcija3':
                        pitanje.opcija_three_count += 1
                        pitanje.save()
            user = request.user
            profil = Profil.objects.filter(id=user.profil.id).first()
            profil.pregledane_ankete += 1
            profil.save()

            popunjena_anketa = get_object_or_404(
                AnketaPopunjena, profil=request.user.profil, anketa=anketa)
            popunjena_anketa.popunjena_anketa = True
            popunjena_anketa.save()
            messages.success(request, f'Hvala, Uspešno ste glasali!')
            return redirect('ankete:rezultat_anketa_profil', pk)

        context = {
            'anketa': anketa,
            'pitanja': pitanja,

        }
        return render(request, 'ankete/glasaj_anketa.html', context)
    else:
        return redirect('ankete:ankete')


@login_required()
@user_passes_test(accepted_check, login_url='account:home', redirect_field_name=None)
def ignorisi_anketa(request, pk):
    anketa = get_object_or_404(Anketa, pk=pk)
    user = request.user
    #profil = Profil.objects.filter(id=user.profil.id).first()
    #print(anketa.id, profil.id)
    anketa_ignorisi = get_object_or_404(AnketaPopunjena,
                                        profil=user.profil.id, anketa=anketa.id, popunjena_anketa=False)
    if request.method == "POST":
        anketa_ignorisi.delete()
        # messages.success(request, f'Uspešno ste ignorisali anketu {anketa}!')
        return redirect('ankete:ankete')
    context = {'item': anketa}
    return render(request, 'ankete/ignorisi_anketa.html', context)


@login_required()
@user_passes_test(accepted_check, login_url='account:home', redirect_field_name=None)
def rezultat_anketa_profil(request, pk):
    anketa = get_object_or_404(Anketa, pk=pk)
    pitanja = AnketaPitanje.objects.filter(anketa_id=pk)
    anketa_popunjena_stanje = AnketaPopunjena.objects.filter(
        anketa=anketa, profil=request.user.profil, popunjena_anketa=True
    )
    if anketa_popunjena_stanje:
        context = {
            'anketa': anketa,
            'pitanja': pitanja
        }
        return render(request, 'ankete/rezultat_anketa_profil.html', context)
    else:
        return redirect('ankete:ankete')
