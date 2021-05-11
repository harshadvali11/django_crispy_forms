from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from app.forms import *
def Contact(request):
    form=ContactForm()
    return render(request,'Contact_form.html',context={'form':form})


def hai(request,name):
    return HttpResponse('hello {}'.format(name))