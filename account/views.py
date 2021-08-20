from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages



def home(request):
    return render(request, 'account/home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Uspesno ste se registrovali!')
            return redirect('account:login')
    else:
        form = UserRegisterForm()
    return render(request, 'account/register.html', {'form': form})


def status(request):
    return render(request, 'account/status.html')
