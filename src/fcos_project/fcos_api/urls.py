from django.urls import path

from . import views

app_name='fcos_api'

urlpatterns = [
	path('hello-view/', views.HelloApiView.as_view()),
]