from django.shortcuts import render, redirect
from .models import Diario
from .forms import DiarioForm
from django.contrib import messages
from django.http import HttpResponseRedirect


def home(request):
    if request.method == "POST":
        form = DiarioForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = Diario.objects.all()
            messages.success(request, ("New diario has been created and added to the list of items."))
            return render(request, 'app/home.html', {'all_items': all_items})

    else:
        all_items = Diario.objects.all()
        return render(request, 'app/home.html', {'all_items': all_items})


def about(request):
    context = {'first_name': 'Guillermo', 'last_name': 'Kastro'}
    return render(request, 'app/about.html', context)

