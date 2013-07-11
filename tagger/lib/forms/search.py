from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.core.validators import validate_email

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class SearchTagForm(forms.Form):
  name = forms.CharField(max_length = 200)

  def __init__(self, *args, **kwargs):
    super(SearchTagForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_id = 'search_tag_form'
    self.helper.form_method = 'post'
    self.helper.form_action = 'submit_tag'
    self.helper.add_input(Submit('submit', 'Search'))