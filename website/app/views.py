from django.shortcuts import render, redirect
from .models import Diario
from .forms import DiarioForm
from django.contrib import messages
#from django.http import HttpResponseRedirect


def home(request):
    if request.method == 'POST':
        form = DiarioForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = Diario.objects.all
            messages.success(request, ("New diario has been created and added to the list of items."))
            return render(request, 'app/home.html', {'all_items': all_items})

    else:
        all_items = Diario.objects.all
        return render(request, 'app/home.html', {'all_items': all_items})


def about(request):
    context = {'first_name': 'Guillermo', 'last_name': 'Kastro'}
    return render(request, 'app/about.html', context)


def delete(request, list_id):
        item = Diario.objects.get(p=list_id)
        item.delete()
        messages.success(request, ("Diario has been deleted from the list of items."))
        return redirect('home')


def cross_off(request, list_id):
        item = Diario.objects.get(pk=list_id)
        item.completed = True
        item.save()
        return redirect('home')


def uncross(request, list_id):
        item = Diario.objects.get(pk=list_id)
        item.completed = False
        item.save()
        return redirect('home')


def edit(request, list_id):
        if request.method == "POST":
            item = Diario.objects.get(pk=list_id)

            form = DiarioForm(request.POST or None, instance=item)

            if form.is_valid():
                form.save()
                messages.success(request, ("Diario has been edited and updated successfully!"))
                return redirect("home")

        else:
            item = Diario.objects.get(pk=list_id)
            return render(request, "app/edit.html", {"item": item})


