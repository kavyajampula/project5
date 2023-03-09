from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def chinna(request):
    return HttpResponse('Chinna is the brother of kavya')