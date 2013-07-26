window.TASK =
  init: ->
    TASK.prepareNewItemForm()
    TASK.focusForm()

  focusForm: ->
    $('#id_name').focus() if $('#id_name').length > 0
    if ('#task_item_name').length > 0
      $('#task_item_name').focus ->
        $(this).animate({ width: '+=250' })
      .blur ->
        $(this).animate({ width: '-=250' })
    return 1

  prepareNewItemForm: ->
    csrf = PDA.getCookie('csrftoken')
    $('.csrfmiddlewaretoken').val(csrf)


TASK.init()