from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from .validators import superuser_check
from profil.models import Profil, Oblast
from .forms import ObavestenjeForm, OblastForm
from radovi.models import ProsledjenRad


@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def profil(request):
    return render(request, 'administrator/admin_profil.html')


@login_required()
@user_passes_test(superuser_check, login_url='account:home', redirect_field_name=None)
def pregled_prijava(request):
    prijave = Profil.objects.all().order_by('-id')
    prosledjen_radovi = ProsledjenRad.objects.filter(zakljucani_odgovori=False)

    broj_radova_na_recenziji = {}
    for prijava in prijave:
        for prosledjen_rad in prosledjen_radovi:
            if prijava == prosledjen_rad.profil:
                try:
                    broj_radova_na_recenziji[prijava] += 1
                except KeyError:
                    broj_radova_na_recenziji[prijava] = 1

    context = {
        'prijave': prijave,
        'broj_radova_na_recenziji': broj_radova_na_recenziji
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
        subject=_('Prihvaćena Prijava'),
        message=_(
            'Poštovani/a, \n \n'
            'Vaša prijava je prihvaćena! \n \n'
            'Uživajte u korišćenju našeg Portala za ocenjivanje naučnih radova.'
        ),
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
        subject=_('Odbijena Prijava'),
        message=_(
            'Poštovani/a, \n \n'
            'Vaša prijava je odbijena! \n \n'
            'Portal za ocenjivanje naučnih radova.'
        ),
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
            if request.POST.get('send_mail'):
                for profil in form.cleaned_data['profil']:
                    send_mail(
                        subject=f'{form.cleaned_data["naslov"]}',
                        message=f'{form.cleaned_data["tekst"]} \n \n'
                        'Portal za ocenjivanje naučnih radova.',
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[profil.user.email]
                    )
                    form.save()
                messages.success(request, _(f'Uspešno poslano obaveštenje i preko mail-a!'))
                return redirect('administrator:profil')
            else:
                form.save()
                messages.success(request, _(f'Uspešno poslano obaveštenje!'))
                return redirect('administrator:profil')
    else:
        form = ObavestenjeForm()
        context = {
            'form': form
        }
    
    return render(request, 'administrator/kreiraj_obavestenje.html', context)


### OBLASTI ###
class ListaOblastiAdmin(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    form_class = OblastForm
    template_name = 'administrator/lista_oblasti_admin.html'

    def test_func(self):
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        kwargs['oblasti'] = Oblast.objects.order_by('-id')
        return super(ListaOblastiAdmin, self).get_context_data(**kwargs)

    def get_success_url(self):
        return reverse('administrator:lista_oblasti_admin')


class IzmeniOblastAdmin(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Oblast
    template_name = 'administrator/izmeni_oblast_admin.html'
    fields = ['naziv']

    def test_func(self):
        return self.request.user.is_superuser

    def get_success_url(self):
        return reverse('administrator:lista_oblasti_admin')


class ObrisiOblastAdmin(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Oblast
    template_name = 'administrator/obrisi_oblast_admin.html'

    def test_func(self):
        return self.request.user.is_superuser

    def get_success_url(self):
        return reverse('administrator:lista_oblasti_admin')

