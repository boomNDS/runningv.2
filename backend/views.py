from django.shortcuts import render
from backend.models import 
from backend.forms import 
# Create your views here.
def index(request):

    context = {
        'page_title': "รายการคำขอลางานของฉัน",
    }
    return render(request, template_name='aindex.html', context=context)

def regist_create_view(request):
    if(request.method == 'POST'):
        form = RegisterForm(request.POST)
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'regist_create.html', context)
