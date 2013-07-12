from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.core.validators import validate_email

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class UpdateTaskForm(forms.Form):
  name = forms.CharField(max_length = 200)
  description = forms.CharField(widget = forms.Textarea())
  completed = forms.BooleanField()
  expected_at = forms.DateTimeField()

  def __init__(self, *args, **kwargs):
    super(NewForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_id = 'upate_task_form'
    self.helper.form_method = 'post'
    self.helper.form_action = 'submit_task'
    self.helper.add_input(Submit('submit', 'Update Task'))