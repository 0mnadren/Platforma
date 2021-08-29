from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail

from .validators import superuser_check
from profil.models import Profil
from .forms import ObavestenjeForm
from django.conf import settings

@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def profil(request):
    return render(request, 'administrator/admin_profil.html')


@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def pregled_prijava(request):
    prijave = Profil.objects.all().order_by('-id')
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

    send_mail(
        subject='Prihvacena Prijava',
        message='Postovani/a, \n \n'
                'Vasa prijava je prihvacena! \n \n'
                'Uzivajte u koriscenju naseg Portala za ocenjivanje naucnih radova.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email]
    )

    return redirect('administrator:pregled_prijava')


@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def prijava_odbijena(request, pk):

    prijava = get_object_or_404(Profil, pk=pk)
    user = prijava.user
    user.profile_accepted = False
    user.save()

    send_mail(
        subject='Odbijena Prijava',
        message='Postovani/a, \n \n'
                'Vasa prijava je odbijena! \n \n'
                'Portal za ocenjivanje naucnih radova.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email]
    )

    return redirect('administrator:pregled_prijava')


### OBAVESTENJA ###

@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def kreiraj_obavestenje(request):
    if request.method == 'POST':
        form = ObavestenjeForm(request.POST or None)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            messages.success(request, f'Uspesno poslano obavestenje!')
            return redirect('administrator:profil')
    else:
        form = ObavestenjeForm()
        context = {
            'form': form
        }
    
    return render(request, 'administrator/kreiraj_obavestenje.html', context)

