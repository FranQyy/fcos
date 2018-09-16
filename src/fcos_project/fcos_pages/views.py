from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm

import requests

# Create your views here.

# def index(request):
#   return render(request, 'fcos_pages/content/index.html')

@login_required
def localisations(request):
  ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
  print(ip_address)
  response = requests.get('http://api.ipstack.com/check?access_key=24eb765a336f5b614aee079d61416188')
  geodata = response.json()
  return render(request, 'fcos_pages/content/localisations.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'city': geodata['city'],
  })

@login_required
def activities(request):
  return render(request, 'fcos_pages/content/activities.html')

@login_required
def profile(request):
  return render(request, 'fcos_pages/content/profile.html')

# def user_login(request):
#   if request.method == 'POST':
#     form = LoginForm(request.POST)
#     if form.is_valid():
#       data = form.cleaned_data
#       email = data['email']
#       password = data['password']
#       user = authenticate(email=email, password=password)
#       if user is not None:
#         if user.is_active:
#           login(request, user)
#           return render(request, 'fcos_pages/content/index.html')
#         else:
#           return HttpResponse('Konto jest zablokowane.')
#       else:
#         return HttpResponse('Nieprawidłowe dane uwierzytelniające.')
#   else:
#     form = LoginForm()
#   return render(request, 'fcos_pages/content/user_login.html', {'form': form})

class SignUp(generic.CreateView):
  form_class = CustomUserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'signup.html'