from django.shortcuts import render

def about(request):
    """ A view for the about page """
    return render(request, 'about.html')