TASK =
  init: ->
    TASK.focusForm()

  focusForm: ->
    $('#id_name').focus() if $('#id_name').length > 0


TASK.init()