from django.http import HttpResponse
from django.shortcuts import render, redirect

from accounts.forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login(request):
    return HttpResponse("Вы зарегистрированы")