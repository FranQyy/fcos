from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .forms import LoginForm
from django.views.generic.edit import UpdateView

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
  return render(request, 'fcos_pages/content/index.html')

@login_required(login_url='/user_login/')
def localisations(request):
  return render(request, 'fcos_pages/content/localisations.html')

@login_required(login_url='/user_login/')
def activities(request):
  return render(request, 'fcos_pages/content/activities.html')

@login_required(login_url='/user_login/')
def profile(request):
  return render(request, 'fcos_pages/content/profile.html')

def user_login(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      email = data['email']
      password = data['password']
      user = authenticate(email=email, password=password)
      if user is not None:
        if user.is_active:
          login(request, user)
          return render(request, 'fcos_pages/content/index.html')
        else:
          return HttpResponse('Konto jest zablokowane.')
      else:
        return HttpResponse('Nieprawidłowe dane uwierzytelniające.')
  else:
    form = LoginForm()
  return render(request, 'fcos_pages/content/user_login.html', {'form': form})

