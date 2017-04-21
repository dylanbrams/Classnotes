#This is the file containing kiln management views.

import os

from KilnData import models
from django.http import HttpResponse
from django.shortcuts import render
from KilnData import KilnDataLogic

def add_kiln(_, kiln_name_in):
    new_kiln = models.Kiln()
    new_kiln.kiln_name= kiln_name_in
    new_kiln.save()
    return HttpResponse(new_kiln.__repr__());
    #return HttpResponse(kiln_name_in)


def add_update_kiln_data(request):
    # add a kiln or update a kiln's data.
    form_data = {
        'kiln_id': request.POST['kiln_id'],
        'kiln_name': request.POST['kiln_name'],
    }
    KilnDataLogic.add_modify_kiln_data(form_data)

    return HttpResponse

def view_kiln_data(request, kiln_id_in):
    this_kiln = models.Kiln.objects\
        .filter(kiln_id= kiln_id_in)
    template_arguments = {}
    if (this_kiln is not None):
        if (this_kiln.count() > 0):
            template_arguments = {
                'kiln_id' : this_kiln[0].kiln_id,
                'kiln_name' : this_kiln[0].kiln_name,
            }
    return render(request, './add_modify_kiln.html', template_arguments)


def view_kiln(request, kiln_name_in):
    this_kiln = models.Kiln.objects\
        .filter(kiln_name = kiln_name_in)
    template_arguments = {
        'kiln_name' : this_kiln[0].kiln_name,
    }
    return render(request, './view_kiln.html', template_arguments)

def add_update_program(request):
    # add a program or update a program's data.
    form_data = {
        'program_id': request.POST['program_id'],
        'program_type': request.POST['program_type'],
        'program_name': request.POST['program_name'],
    }
    KilnDataLogic.add_modify_program_data(form_data)

    return HttpResponse

def view_program_data(request, program_id_in):
    this_program = models.Program.objects \
        .filter(program_id=program_id_in)
    template_arguments = {}
    if (this_program is not None):
        if (this_program.count() > 0):
            template_arguments = {
                'program_id': this_program[0].program_id,
                'program_type': this_program[0].program_type,
                'program_name': this_program[0].program_name,
            }
    return render(request, './add_modify_kiln.html', template_arguments)


def home (request):
    template_arguments = {

    }
    return render(request, './home.html', template_arguments)

def view_env_test(request):
    this_env = os.environ['ENVIRON_TEST_STRING']
    return HttpResponse(this_env)