from django.shortcuts import render

# Create your views here.

def view_workshops(request):
    """ A view that renders the workshops page """

    return render(request, 'workshops/workshops.html')