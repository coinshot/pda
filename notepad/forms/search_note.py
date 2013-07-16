from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.core.validators import validate_email

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class SearchNoteForm(forms.Form):
  keyword = forms.CharField()

  def __init__(self, *args, **kwargs):
    super(SearchNoteForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_id = 'search_note_form'
    self.helper.form_method = 'post'
    self.helper.add_input(Submit('submit', 'Search'))