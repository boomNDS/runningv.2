from django.shortcuts import render, redirect
from backend.models import *
from .forms import *
from django.forms import formset_factory
# Create your views here.


def registerfinish(request):

    context = {
        'e': request.session.get('my_email', ''),
        'payment': RegisterInfo.objects.get(user_email=request.session.get('my_email', '')),
        # 'isregis': RegisterInfo.objects.filter(user_email=request.session.get('my_email', '')).exists()
    }
    return render(request, template_name='registerfinish.html', context=context)


def index(request):

    context = {
        'e': request.session.get('my_email', ''),
    }
    return render(request, template_name='aindex.html', context=context)



def edit_regist_view(request):
    if request.method == 'GET':
        regist = RegisterInfo.objects.get(user_email=request.session['my_email'])
        form = RegisterForm(initial={
                    'user_email': getattr(regist, 'user_email'),
                    'event_id':getattr(regist, 'event_id'),
                    'running_type_id': getattr(regist, 'running_type_id'),
                    'payment_date':getattr(regist, 'payment_date'),
                    'pay_inSlip': getattr(regist, 'pay_inSlip'),
                    })
        context = {
                    'form': form,
                    'e': request.session.get('my_email', ''),
                }
        return render(request, 'edit_regist.html', context)

    elif request.method == 'POST':
        regist = RegisterInfo.objects.get(
            user_email=request.session['my_email'])
        form = RegisterForm(request.POST, instance=regist)
        if form.is_valid:
            # update record
            instance = form.save()
            running_type_id = form.cleaned_data['running_type_id']
            # edit solo runner
            if(str(running_type_id) == 'solo runner'):
                    runner = Runner.objects.get(regist_id=regist.pk)
                    solo_runner = SoloRunner.objects.get(runner_bib=runner.pk)
                    soloform = SoloRunnerform(
                        initial={
                            'bus': getattr(solo_runner, 'bus'),
                            'resident':getattr(solo_runner, 'resident'),
                            'runner_bib': getattr(solo_runner, 'runner_bib'),
                        }
                    )
                    RunnerFormSet = formset_factory(RunnerForm, extra=0)
                    formset = RunnerFormSet(initial=[
                        {
                            'regist_id': instance.pk,
                            'size': getattr(runner, 'size'),
                            'runner_firstname': getattr(runner, 'runner_firstname'),
                            'runner_lastname': getattr(runner, 'runner_lastname'),
                            'sex': getattr(runner, 'sex'),
                            'age': getattr(runner, 'age')
                        }
                    ])
                    context = {
                        'form': soloform,
                        'formset': formset,
                        'e': request.session.get('my_email', ''),
                    }
                    return render(request, 'solo_runner_create.html', context)
            else:
                # just throw to regist but still need to implement
                form = Teamform()
                context = {
                    'form': form,
                    'e': request.session.get('my_email', ''),
                }
                return render(request, 'team_create.html', context)
                
                
        # when edit fail just do it again
        return render(request, 'edit_regist.html')

            



def regist_create_view(request):
    if RegisterInfo.objects.filter(user_email=request.session.get('my_email', '')).exists():
        context = {
                'e': request.session.get('my_email', ''),
                'payment': RegisterInfo.objects.get(user_email=request.session.get('my_email', '')),
                # 'isregis': RegisterInfo.objects.filter(user_email=request.session.get('my_email', '')).exists()
            }

        return render(request, template_name='registerfinish.html', context=context)
    
    elif request.method == 'POST':
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
                        'formset': formset,
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
    if(request.method == 'POST'):
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
    if(request.method == 'POST'):
        form = Teamform(request.POST)
        if(form.is_valid):
            instance = form.save()
            team_type = form.cleaned_data['team_type']
            registinfo = RegisterInfo.objects.get(
                user_email=request.session['my_email'])
            if str(team_type) == 'team need runner':
                RunnerFormSet = formset_factory(RunnerForm, extra=0)
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
        registinfo = RegisterInfo.objects.get(
            user_email=request.session('my_email'))
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
        RunnerFormSet = formset_factory(RunnerForm, extra=0)
        formset = RunnerFormSet(request.POST)
        if formset.is_valid():
            for runner_form in formset:
                instance = runner_form.save()
            form = ManagerForm(initial={'team_id': instance.team_id})
            diverForm = Driverform(initial={'team_id': instance.team_id})
            
            context = {
                'form': form,
                'diverForm': diverForm,
                'e': request.session.get('my_email', ''),
                'payment': RegisterInfo.objects.get(user_email=request.session.get('my_email', '')),
            }
        if str(team_type) == 'team need runner':
            return render(request, 'manager_create.html', context)
        else:
            return render(request, 'registerfinish.html')

    else:
        form = ManagerForm()
        context = {
            'form': '',
            'e': request.session.get('my_email', ''),
        }
        return render(request, 'manager_create.html', context)


def solo_runner_create_view(request):
    
    # for update chelk if already have runner in this regist
    if Runner.objects.filter(regist_id=RegisterInfo.objects.get(user_email=request.session['my_email']).pk).exists():
        regist = RegisterInfo.objects.get(user_email=request.session['my_email'])
        runner = Runner.objects.get(regist_id=regist.pk)
        solo_runner = SoloRunner.objects.get(runner_bib=runner.pk)
        form = SoloRunnerform(request.POST, instance=solo_runner)
        
        if form.is_valid:
            # update record
            #this is solorunner
            form.save()
            # this is runner
            # RunnerFormSet = formset_factory(RunnerForm, extra=0)
            RunnerFormSet = formset_factory(RunnerForm, extra=0)
            formset = RunnerFormSet(request.POST)
 
            if formset.is_valid():
                for runner_form in formset:
                    runner.runner_firstname  = runner_form.cleaned_data['runner_firstname']
                    runner.size = runner_form.cleaned_data['size']
                    runner.age = runner_form.cleaned_data['age']
                    runner.runner_lastname = runner_form.cleaned_data['runner_lastname']
                    runner.regist_id = runner_form.cleaned_data['regist_id']
                    runner.sex = runner_form.cleaned_data['sex']
                    runner.save()
                context = {
                        'e': request.session.get('my_email', ''),
                        'payment': RegisterInfo.objects.get(user_email=request.session.get('my_email', '')),
                    }
                return render(request, template_name='registerfinish.html', context=context)
    else:    
        RunnerFormSet = formset_factory(RunnerForm, extra=0)
        if(request.method == 'POST'):
            form = SoloRunnerform(request.POST)
            formset = RunnerFormSet(request.POST)
            if(form.is_valid):
                solo = form.save(commit=False)
                RunnerFormSet = formset_factory(RunnerForm, extra=0)
                formset = RunnerFormSet(request.POST)

            # runner have to be saved before solo becasuse solorunner need pk from runner that have to be saved in DB
                if formset.is_valid():
                    for runner_form in formset:
                        instance = runner_form.save()
                        solo.runner_bib = instance
                        solo.save()
                    context = {
                        'e': request.session.get('my_email', ''),
                        'payment': RegisterInfo.objects.get(user_email=request.session.get('my_email', '')),
                    }
                    return render(request, template_name='registerfinish.html', context=context)

        else:
            form = SoloRunnerform()
            RunnerFormSet = formset_factory(RunnerForm, extra=0)
            registinfo = RegisterInfo.objects.get(
                user_email=request.session('my_email'))
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
    if(request.method == 'POST'):
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
