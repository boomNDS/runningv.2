from django.shortcuts import render

# Create your views here.
def index(request):

    context = {
        'page_title': "รายการคำขอลางานของฉัน",
    }
    return render(request, template_name='index.html', context=context)