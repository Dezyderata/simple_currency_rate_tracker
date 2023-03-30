from django.shortcuts import render


def currency_rate(request):
    return render(request, "currency_rate/currency_rate.html")

