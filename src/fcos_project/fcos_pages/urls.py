from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.auth.views import LogoutView

from django.views.generic.base import TemplateView

app_name='fcos_pages'


urlpatterns = [
	path('', TemplateView.as_view(template_name='index.html'), name='index'),
	path('localisations/', views.localisations, name='localisations'),
	path('events/', views.events, name='events'),
	path('profile/', views.profile, name='profile'),
	path('signup/', views.SignUp.as_view(), name='signup'),

]