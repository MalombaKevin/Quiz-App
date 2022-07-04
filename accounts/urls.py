from accounts.api import LoginAPI, RegisterAPI, UserAPI
from django.urls import path


urlpatterns = [
	path("login/", LoginAPI.as_view(),name='login'),
	path("register/", RegisterAPI.as_view(), name='register'),
	path("user/", UserAPI.as_view(), name='user')
]