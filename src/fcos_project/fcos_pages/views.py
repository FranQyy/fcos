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

from decouple import config
# Create your views here.

# def index(request):
#   return render(request, 'fcos_pages/content/index.html')

@login_required
def localisations(request):
  ipstack_apikey = config('ipstack_apikey')
  response = requests.get('http://api.ipstack.com/check?access_key={0}'.format(ipstack_apikey))
  geodata = response.json()
  return render(request, 'fcos_pages/content/localisations.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'region_name': geodata['region_name'],
        'city': geodata['city'],
        'latitude': geodata['latitude'],
        'longitude': geodata['longitude'],
  })

from datetime import datetime

@login_required
def events(request):
  ipstack_apikey = config('ipstack_apikey')
  response = requests.get('http://api.ipstack.com/check?access_key={0}'.format(ipstack_apikey))
  position = response.json()

  n2yo_apikey = config('n2yo_apikey')
  response = requests.get('http://www.n2yo.com/rest/v1/satellite/visualpasses/25544/{0}/{1}/0/7/60/&apiKey={2}'.format(position['latitude'],position['longitude'],n2yo_apikey))
  prediction = response.json()
  print(prediction)

  return render(request, 'fcos_pages/content/events.html', {

    'prediction1_risetime': datetime.utcfromtimestamp(prediction['passes'][0]['startUTC']).strftime('%Y-%m-%d %H:%M:%S'),
    'prediction2_risetime': datetime.utcfromtimestamp(prediction['passes'][1]['startUTC']).strftime('%Y-%m-%d %H:%M:%S'),
    'prediction3_risetime': datetime.utcfromtimestamp(prediction['passes'][2]['startUTC']).strftime('%Y-%m-%d %H:%M:%S'),
    'position': position['latitude'],
    'position2': position['longitude'],
  })

@login_required
def profile(request):
  user = request.user
  return render(request, 'fcos_pages/content/profile.html', {'user': user})

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