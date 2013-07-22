from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from lib.mixins.forms import TaggedFormMixin

from ..models import Task


class TaskForm(TaggedFormMixin, forms.ModelForm):
  tags = forms.CharField(required = False)

  class Meta:
    model = Task
    fields = ['name', 'description', 'expected_at']
    widget = {
      'note': forms.Textarea(),
      'expected_at': forms.DateTimeInput(),
    }

  def __init__(self, *args, **kwargs):
    super(TaskForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_id = 'task_form'
    self.helper.form_method = 'post'
    self.helper.add_input(Submit('submit', 'Submit Task'))
