from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_workshops, name='view_workshops'),
    path('', views.workshopapply, name='workshopapply')
]
