from django.http import HttpResponse
from django.shortcuts import render


def default(request):
    return render(request, 'ajax/default.html')
