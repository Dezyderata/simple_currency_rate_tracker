from django.http import HttpResponse
from django.shortcuts import render


def banks(request):
    return render(request, "banks/banks.html")
