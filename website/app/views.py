from django.shortcuts import render, redirect
from .models import Diario
from .forms import DiarioForm
from django.contrib import messages
from django.http import HttpResponseRedirect


def home(request):
        if request.method == 'POST':
                form = DiarioForm(request.POST or None)

                if form.is_valid():
                        form.save()
                        all_items = Diario.objects.all()
                        messages.success(request, ("Diario Has Successfully Been Added To Journal!"))
                        return render(request, 'home.html', {'all_items': all_items})

        else:
                all_items = Diario.objects.all()
                return render(request, 'home.html', {'all_items': all_items})


def about(request):
        context = {'first_name': 'Sir William', 'last_name': 'Kastrato'}
        return render(request, 'about.html', context)


def delete(request, list_id):
        item = Diario.objects.get(pk=list_id)
        item.delete()
        messages.success(request, ('Diario has been deleted successfully from Journal'))
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
        if request.method == 'POST':
                item = Diario.objects.get(pk=list_id)

                form = DiarioForm(request.POST or None, instance=item)

                if form.is_valid():
                        form.save()
                        messages.success(request, ('Diario from Journal has been updated successfully.'))
                        return redirect('home')

        else:
                item = Diario.objects.get(pk=list_id)
                return render(request, 'edit.html', {'item': item})
