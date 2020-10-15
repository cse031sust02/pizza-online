from django.shortcuts import redirect, render

from .forms import ManagerRegistrationForm


def register(request):
    if request.method == 'POST':
        form = ManagerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store-dashboard')
    else:
        form = ManagerRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
