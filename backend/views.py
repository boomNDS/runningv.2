from django.shortcuts import render
from backend.models import *
from .forms import *
from django.forms import formset_factory
# Create your views here.
def registerfinish(request):

    context = {
        'e': request.session.get('my_email', ''),
        'payment': RegisterInfo.objects.get(user_email=request.session.get('my_email', '')) 
    }
    return render(request, template_name='registerfinish.html', context=context)

def index(request):

    context = {
        'e': request.session.get('my_email', ''),
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
                    'formset':formset,
                    'e': request.session.get('my_email', ''),
                }
                return render(request, 'solo_runner_create.html', context)

            else:
                form = Teamform()
                context = {
                    'form': form,
                    'e': request.session.get('my_email', ''),
                }
                return render(request, 'team_create.html', context)

            
    else:
        form = RegisterForm(initial={
            'user_email': request.session['my_email']
        })
    context = {
        'form': form,
        'e': request.session.get('my_email', ''),
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
        'form': form,
        'e': request.session.get('my_email', ''),
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
        'form': form,
        'e': request.session.get('my_email', ''),
    }
    return render(request, 'manager_create.html', context)
team_type = ""
def team_create_view(request):
    if(request.method=='POST'):
        form = Teamform(request.POST)
        if(form.is_valid):
            instance =  form.save()
            team_type = form.cleaned_data['team_type']
            registinfo = RegisterInfo.objects.get(user_email= request.session['my_email'])
            if str(team_type) == 'team need runner':
                RunnerFormSet = formset_factory(RunnerForm, extra=7)
                formset = RunnerFormSet(initial=[
                {
                    'team_id': instance.pk,
                    'regist_id': registinfo.pk,
                }, {
                    'team_id': instance.pk,
                    'regist_id': registinfo.pk,
                    
                }, {
                    'team_id': instance.pk,
                    'regist_id': registinfo.pk,
                    
                }, {
                    'team_id': instance.pk,
                    'regist_id': registinfo.pk,
                    
                }, {
                    'team_id': instance.pk,
                    'regist_id': registinfo.pk,
                    
                }, {
                    'team_id': instance.pk,
                    'regist_id': registinfo.pk,
                    
                }, {
                    'team_id': instance.pk,
                    'regist_id': registinfo.pk,
                    
                }, {
                    'team_id': instance.pk,
                    'regist_id': registinfo.pk,
                    
                }
                ])
            else:
                RunnerFormSet = formset_factory(RunnerForm, extra=0)
                formset = RunnerFormSet(initial=[
                {
                    'team_id': instance.pk,
                    'regist_id': registinfo.pk,
                }
                ])
        context = {
        'formset': formset,
        'team_type': str(team_type),
        'e': request.session.get('my_email', ''),
        }
        return render(request, 'team_for_runner_create.html', context)
    else:
        form = Teamform()
        RunnerFormSet = formset_factory(RunnerForm, extra=7)
        registinfo = RegisterInfo.objects.get(user_email= request.session('my_email'))
        formset = RunnerFormSet(initial=[
            {
                'regist_id': registinfo.pk,
                'regist_id': registinfo.pk,
            }, {
                'regist_id': registinfo.pk,
            }, {
                'regist_id': registinfo.pk,
            }, {
                'regist_id': registinfo.pk,
            }, {
                'regist_id': registinfo.pk,
            }, {
                'regist_id': registinfo.pk,
            }, {
                'regist_id': registinfo.pk,
            }, {
                'regist_id': registinfo.pk,
            }
        ])
    context = {
        'form': form,
        'formset': formset,
        'e': request.session.get('my_email', ''),
    }
    return render(request, 'team_for_runner_create.html', context)


def team_for_runner_create_view(request):
    if(request.method=='POST'):
        if str(team_type) == 'team need runner':
             RunnerFormSet = formset_factory(RunnerForm, extra=7)
        else:
             RunnerFormSet = formset_factory(RunnerForm, extra=0)
        formset = RunnerFormSet(request.POST)
        if formset.is_valid():
            for runner_form in formset:
                instance =runner_form.save()
            form = ManagerForm(initial={'team_id': instance.team_id})
            diverForm = Driverform(initial={'team_id': instance.team_id})
            context = {
                'form': form,
                'diverForm':diverForm,
                'e': request.session.get('my_email', ''), 
            }
        return render(request, 'manager_create.html', context)

    else:
        form = ManagerForm()
        context = {
            'form': '',
            'e': request.session.get('my_email', ''),
            }
        return render(request, 'manager_create.html', context)




def solo_runner_create_view(request):
    RunnerFormSet = formset_factory(RunnerForm, extra=0)
    if(request.method=='POST'):
        form = SoloRunnerform(request.POST)
        formset = RunnerFormSet(request.POST)
        if(form.is_valid):
            solo = form.save(commit=False)
            RunnerFormSet = formset_factory(RunnerForm, extra=0)
            formset = RunnerFormSet(request.POST)
            if formset.is_valid():
                for runner_form in formset:
                    instance =   runner_form.save()
                    solo.runner_bib = instance
                    solo.save()
                context = {
                    'e': request.session.get('my_email', ''),
                    'payment': RegisterInfo.objects.get(user_email=request.session.get('my_email', '')) 
                }
                return render(request, 'registerfinish.html')

    else:
        form = SoloRunnerform()
        RunnerFormSet = formset_factory(RunnerForm, extra=0)
        registinfo = RegisterInfo.objects.get(user_email= request.session('my_email'))
        formset = RunnerFormSet(initial=[
                    {
                        'regist_id': registinfo.pk,
                    }
                ])
    context = {
        'form': form,
        'formset': formset,
        'e': request.session.get('my_email', ''),
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
        'form': form,
        'e': request.session.get('my_email', ''),
        
    }
    return render(request, 'driver_create.html', context)


