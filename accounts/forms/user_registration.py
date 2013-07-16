from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.core.validators import validate_email

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class UserRegistrationForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']

  def __init__(self, *args, **kwargs):
    super(UserRegistrationForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_id = 'signup_form'
    self.helper.form_method = 'post'
    self.helper.add_input(Submit('submit', 'Signup'))
