from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import UserRegistration

def register(request):
    if request.method == "POST":
        form = UserRegistration(request.POST);
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username');
            return redirect('home')
    else:
        form = UserRegistration()
    return render(request, 'accounts/registration.html', {'form': form})