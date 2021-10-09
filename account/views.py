from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _


def home(request):
    if request.user.is_superuser:
        return render(request, 'administrator/admin_profil.html')
    else:
        return render(request, 'account/home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Uspešno ste se registrovali!'))
            return redirect('account:login')
    else:
        form = UserRegisterForm()
    return render(request, 'account/register.html', {'form': form})


@login_required()
def status(request):
    return render(request, 'account/status.html')
