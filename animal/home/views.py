from django.shortcuts import render

from .forms import UserRegistrationForm

# Create your views here.
def home(request):
    return render(request, 'home/home.html')
def registration(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'home/signin.html', {'new_user': new_user})
            
    else:
        user_form = UserRegistrationForm()
    return render(request, 'home/registration.html', {'user_form': user_form})
def signin(request):
    
    return render(request, 'home/signin.html')