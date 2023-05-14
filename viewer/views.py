from django.shortcuts import render, redirect
from django.contrib.auth import logout
from viewer.forms import SignUpForm


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = SignUpForm()
    return render(request, 'registration.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('homepage')


def homepage(request):
    context = {
    }
    return render(request, 'homepage.html', context)
