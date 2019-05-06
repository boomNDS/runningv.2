from django.shortcuts import render
from backend.models import *
from .forms import *
from django.forms import formset_factory
# Create your views here.
def registerfinish(request):

    context = {
        'page_title': "รายการคำขอลางานของฉัน",
    }
    return render(request, template_name='registerfinish.html', context=context)

def index(request):

    context = {
        'page_title': "รายการคำขอลางานของฉัน",
    }
    return render(request, template_name='aindex.html', context=context)

def regist_create_view(request):
    if(request.method == 'POST'):
        form = RegisterForm(request.POST)
        if(form.is_valid):
            instance = form.save()
            running_type_id = form.cleaned_data['running_type_id']
            if(str(running_type_id) == 'solo runner'):
                soloform = SoloRunnerform()
                RunnerFormSet = formset_factory(RunnerForm, extra=0)
                formset = RunnerFormSet(initial=[
                    {
                        'regist_id': instance.pk,
                    }
                ])
                context = {
                    'form': soloform,
                    'formset':formset
                }
                return render(request, 'solo_runner_create.html', context)

            else:
                form = Teamform()
                RunnerFormSet = formset_factory(RunnerForm, extra=7)
                formset = RunnerFormSet(initial=[
                    {
                        'regist_id': instance.pk,
                    }, {
                        'regist_id': instance.pk,
                    }, {
                        'regist_id': instance.pk,
                    }, {
                        'regist_id': instance.pk,
                    }, {
                        'regist_id': instance.pk,
                    }, {
                        'regist_id': instance.pk,
                    }, {
                        'regist_id': instance.pk,
                    }, {
                        'regist_id': instance.pk,
                    }
                ])
                context = {
                    'form': form,
                    'formset': formset
                }
                return render(request, 'team_create.html', context)

            
    else:
        form = RegisterForm(initial={
            'user_email': request.session['my_email']
        })
    context = {
        'form': form
    }
    return render(request, 'regist_create.html', context)


def runner_create_view(request):
    if(request.method == 'POST'):
        form = RunnerForm(request.POST)
        if(form.is_valid):
            form.save()
    else:
        form = RunnerForm()
    context = {
        'form': form
    }
    return render(request, 'runner_create.html', context)

def manager_create_view(request):
    if(request.method=='POST'):
        form = ManagerForm(request.POST)
        if(form.is_valid):
            form.save()
    else:
        form = ManagerForm()
    context = {
        'form': form
    }
    return render(request, 'manager_create.html', context)

def team_create_view(request):
    if(request.method=='POST'):
        form = Teamform(request.POST)
        if(form.is_valid):
            form.save()
    else:
        form = Teamform()
    context = {
        'form': form
    }
    return render(request, 'team_create.html', context)

def solo_runner_create_view(request):
    if(request.method=='POST'):
        form = SoloRunnerform(request.POST)
        if(form.is_valid):
            form.save()
    else:
        form = SoloRunnerform
    context = {
        'form': form
    }
    return render(request, 'solo_runner_create.html', context)


def driver_create_view(request):
    if(request.method=='POST'):
        form = Driverform(request.POST)
        if(form.is_valid):
            form.save()
    else:
        form = Driverform
    context = {
        'form': form
    }
    return render(request, 'driver_create.html', context)


