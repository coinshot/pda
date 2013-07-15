from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.core.validators import validate_email

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class UserRegistrationForm(forms.Form):
  first_name = forms.CharField(max_length = 30)
  last_name = forms.CharField(max_length = 30)
  email = forms.EmailField(max_length = 75)
  username = forms.CharField(max_length = 200)
  password = forms.CharField(max_length = 128)

  def __init__(self, *args, **kwargs):
    super(ContactForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_id = 'contact_form'
    self.helper.form_method = 'post'
    self.helper.form_action = 'submit_survey'
    self.helper.add_input(Submit('submit', 'Send Enquiry'))