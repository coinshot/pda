NOTE =
  init: ->
    NOTE.focusForm()

  focusForm: ->
    $('#id_name').focus() if $('#id_name').length > 0


NOTE.init()