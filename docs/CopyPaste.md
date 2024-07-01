{% extends 'app/base.html' %}


<title>{% block title %}Entre du Diario!{% endblock title %}</title>


{% block content %}
<br />
<h1 style="padding-left: 20%; text-decoration: underline; font-family: Apple Chancery;">Acerca de mi solicitud de diario</h1>
<br />
<h4 style="padding-left: 2.5%; font-family: Apple Chancery;">Hola! Mi nombre es "{{ first_name }} {{ last_name }}". Y soy estoy aqui para compartir mi applicacion Diario!</h4>
<br />
<div class="" style="border: 1.5px double rgba(0, 0, 255, 0.1);">
    <span style="margin-left: 5%; margin-right: 5%;">
        <p style="padding-left: 4.5%; padding-right: 4.5%;">
        Este aplicacion fue creade para hacer mi vida mas facil permitiendome organizar y estructurar mis estudios. Ademas, crear esta aplicacion me permitiria aprender mas sobre programacion. Este proyecto sera uno de muchos proyectos personales. Mi objectivo final es aprender muy bien React y Django, para fullstack. Llevo casi dos anos y medio programado por mi cuenta. Llevo casi dos anos dando vueltas probando diferentes tecnologias. Porque no estaba segura de lo que me gustaba y disfrutaba. Desde moviles, juegos, finalmente hasta desarrollo web. Disfrute bastante todo lo que toque que fue programacion y codificacion, estaba fascinado! Al principio aprendi no por dinero, sino para consequir un trabajo. Sino porque en realidad estaba disfrutando lo que estaba haciendo. Pero ahora, despues de mas de dos anos de exploracion, es hora de centrarse y finalmente me decidi por una pila tecnologica. Estoy aprendiendo Django y React al mismo tiempo. La mayoria de mis habilidades estan en Django. Pero tambien tengo algunas habilidades en React. Con suerte, para el proximo ano deberia poder crear una aplicacion CRUD completa con React y Django y poder slicitar trabajos a mediados del proximo ano, gracias!
        </p>
    </span>
</div>
{% endblock content %}


------------------------------------------------------------------------------------------------------------------------
home.html FILE:

{% extends 'app/base.html' %}

{% block content %}
<div>
    {% if all_items %}
    <table class="table table-striped table-hover table-bordered">
        <thead class="table-dark">
            {% for things in all_items %}
                {% if things.completed %}
                <tr class="table-secondary">
                    <td class="striker"><a href="{% url 'edit' things.id %}">{{ things.item }}</a></td>
                    <td><a href="{% url 'time_stamp' things.id %}">{{ things.item }}</a></td>
                    <td><a href="{% url 'uncross' things.id %}">uncross</a></td>
                    <td><a href="{% url 'delete' things.id %}">Delete</a></td>
                </tr>
            {% else %}
                <tr>
                    <td><a href="{% url 'edit' things.id %}">{{ things.item }}</a></td>
                    <td><a href="{% url 'time_stamp' things.id %}">{{ things.item }}</a></td>
                    <td><a href="{% url 'cross_off' things.id %}">{{ things.item }}</a></td>
                    <td><a href="{% url 'delete' things.id %}">{{ things.item }}</a></td>
                </tr>
                {% endif %}
            {% endfor %}
        </thead>
    </table>
    {% endif %}
</div>

{% endblock content %}




------------------------------------------------------------------------------------------------------------------------

views.py FILE:

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







