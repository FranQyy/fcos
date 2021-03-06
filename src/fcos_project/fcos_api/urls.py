from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name='fcos_api'

router = DefaultRouter()

router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserViewSet)
router.register('login', views.LoginViewSet, base_name='login')
router.register('location', views.LocationViewSet)

urlpatterns = [
	path('hello-view/', views.HelloApiView.as_view()),
	path('', include(router.urls)),
]