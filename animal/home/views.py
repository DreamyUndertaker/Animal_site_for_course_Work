from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from .forms import SignUpForm


# Create your views here.

def registration(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/main')
    else:
        form = SignUpForm()
    return render(request, 'home/registration.html', {'form': form})
def home(request):
    return render(request, 'home/home.html')