from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render
from .forms import UserSignupForm


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your account has been created! Welcome to Tiny Url.")
            return redirect('login')
    else:
        form = UserSignupForm()
    return render(request, 'users/signup.html', {'form': form})