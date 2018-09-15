from django import forms
       
class LoginForm(forms.Form):
  email = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput)

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from fcos_api.models import User

class CustomUserCreationForm(UserCreationForm):

  class Meta(UserCreationForm.Meta):
    model = User
    fields = ('first_name', 'email')