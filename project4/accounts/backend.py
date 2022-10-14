from django.contrib.auth.models import Account

class EmailAuthbackend():
  def authenticate(self, email, password):    
    try:
      user = Account.objects.get(email=email)
      if user.check_password(password):
        return user
      else:
        return None
    except Account.DoesNotExist:
      return None
    except Exception as e:
      return None

  def get_user(self, user_id):
    try:
      user = Account.objects.get(sys_id=user_id)
      if user.is_active:
        return user
      return None
    except Account.DoesNotExist:
      return None