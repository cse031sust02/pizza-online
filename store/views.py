from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home(request):
    return render(request, 'store/dashboard.html')


@login_required
def setup(request):
    return render(request, 'store/setup.html')


@login_required
def items(request):
    return render(request, 'store/items.html')


@login_required
def orders(request):
    return render(request, 'store/orders.html')
