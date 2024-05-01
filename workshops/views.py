from django.shortcuts import render, redirect
from .models import Workshops, WorkshopApply
from .forms import ApplyForm

# Create your views here.

def view_workshops(request):
    """ A view that renders the workshops page """

    workshops = Workshops.objects.all()

    context = {
        'workshops': workshops,
    }

    return render(request, 'workshops/workshops.html', context)

def workshopapply(request):
    """ View for application form """
    if request.method == 'POST':
        form = ApplyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workshops/thankyou.html')
    else:
        form = ApplyForm()
    
    context = {
        'form': form,
    }

    return render(request, 'workshops/workshopapply.html', context)

def thankyou(request):
    """ A view that renders the thank you page """

    context = {
        'thankyou': thankyou,
    }

    return render(request, 'workshops/thankyou.html', context)