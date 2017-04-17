#This is the file containing kiln management views.

from django.http import HttpResponse
from . import models
from django.shortcuts import render

def add_kiln(_, kiln_name_in):
    new_kiln = models.Kiln()
    new_kiln.kiln_name= kiln_name_in
    new_kiln.save()
    return HttpResponse(new_kiln.__repr__());
    #return HttpResponse(kiln_name_in)

def view_kiln(request, kiln_name_in):
    this_kiln = models.Kiln.objects\
        .filter(kiln_name = kiln_name_in)
    template_arguments = {
        'kiln_name' : this_kiln[0].kiln_name,
    }
    return render(request, './view_kiln.html', template_arguments )