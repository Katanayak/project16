from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def guru(request,baro):
    return HttpResponse(f'<h1>hai Happy Sankranthi {baro}</h1>')