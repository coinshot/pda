from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.core.validators import validate_email

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from lib.mixins.views import TaggedFormMixin

from ..models.note import Note


class NoteForm(TaggedFormMixin, forms.ModelForm):
  tags = forms.CharField(required = False)

  class Meta:
    model = Note
    fields = ['name', 'note']
    widget = {
      'note': forms.Textarea(),
    }

  def __init__(self, *args, **kwargs):
    super(NoteForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_id = 'note_form'
    self.helper.form_method = 'post'
    self.helper.add_input(Submit('submit', 'Submit Note'))
