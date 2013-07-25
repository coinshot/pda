from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class UpdateTagForm(forms.Form):
  name = forms.CharField(max_length = 200)

  def __init__(self, *args, **kwargs):
    super(UpdateTagForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_id = 'update_tag_form'
    self.helper.form_method = 'post'
    self.helper.form_action = 'submit_tag'
    self.helper.add_input(Submit('submit', 'Update Tag'))