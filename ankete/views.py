from django.shortcuts import render

from .models import Anketa
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required()
def ankete(request):

    ankete = Anketa.objects.all()
    context = {
        'ankete': ankete
    }

    return render(request, 'ankete/ankete.html', context)