from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class NewTagForm(forms.Form):
  name = forms.CharField(max_length = 200)

  def __init__(self, *args, **kwargs):
    super(NewTagForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_id = 'new_tag_form'
    self.helper.form_method = 'post'
    self.helper.form_action = 'submit_tag'
    self.helper.add_input(Submit('submit', 'Create Tag'))