from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name='fcos_api'

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

router.register('profile', views.UserViewSet)

urlpatterns = [
	path('hello-view/', views.HelloApiView.as_view()),
	path('', include(router.urls)),
]