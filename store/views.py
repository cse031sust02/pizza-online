from django.shortcuts import render


def home(request):
    return render(request, 'store/dashboard.html')


def orders(request):
    return render(request, 'store/orders.html')
