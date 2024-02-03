from django.shortcuts import redirect, render

from .forms import UserRegistrationForm

# Create your views here.
def home(request):
    return render(request, 'home/home.html')
def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST);
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username');
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'home/registration.html', {'form': form})
def signin(request):
    return render(request, 'home/signin.html')