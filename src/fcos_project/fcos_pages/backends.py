from fcos_api.models import User
import logging
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

class MyAuthBackend(ModelBackend):
  def authenticate(self, request, email=None, password=None, **kwars):    
    UserModel = get_user_model()
    try:
      user = UserModel.objects.get(email=email)
    except UserModel.DoesNotExist:
      return None
    else:
      if check_password(password, user.password):
        return user

    return None

  def get_user(self, user_id):
    try:
      user = User.objects.get(id=user_id)
      if user.is_active:
        return user
      return None
    except User.DoesNotExist:
      logging.getLogger("error_logger").error("user with %(user_id)d not found")
      return None
