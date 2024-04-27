from django.shortcuts import render
from .models import Workshops

# Create your views here.

def view_workshops(request):
    """ A view that renders the workshops page """

    workshops = Workshops.objects.all()

    context = {
        'workshops': workshops,
    }

    return render(request, 'workshops/workshops.html', context)