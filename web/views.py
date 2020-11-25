from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ManagerRegistrationForm


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = ManagerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('web-dashboard')
    else:
        form = ManagerRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'web/dashboard.html')


@login_required
def setup(request):
    return render(request, 'web/setup.html')


@login_required
def items(request):
    return render(request, 'web/items/list.html')


@login_required
def orders(request):
    return render(request, 'web/orders.html')
