from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.auth.views import LogoutView

app_name='fcos_pages'


urlpatterns = [
	path('', views.index, name='index'),
	path('localisations/', views.localisations, name='localisations'),
	path('activities/', views.activities, name='activities'),
	path('profile/', views.profile, name='profile'),
	path('user_login/', views.user_login, name='user_login'),

]