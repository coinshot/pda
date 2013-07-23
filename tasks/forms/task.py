from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from lib.mixins.forms import TaggedFormMixin

from ..models import Task


class TaskForm(TaggedFormMixin, forms.ModelForm):
  tags = forms.CharField(required = False)

  class Meta:
    model = Task
    fields = ['name', 'description', 'expected_at', 'tags', 'completed']
    widget = {
      'description': forms.Textarea(),
      'expected_at': forms.DateTimeInput(),
    }

  def __init__(self, *args, **kwargs):
    super(TaskForm, self).__init__(*args, **kwargs)
    self.fields['expected_at'].required = False
    self.fields['expected_at'].label = 'Due Date'
    self.fields['description'].widget.attrs['class'] = 'short-description'
    self.helper = FormHelper()
    self.helper.form_id = 'task_form'
    self.helper.form_method = 'post'
    self.helper.add_input(Submit('submit', 'Submit Task'))
