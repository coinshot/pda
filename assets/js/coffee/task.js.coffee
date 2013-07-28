window.TASK =
  init: ->
    TASK.setupNewItemForm()
    TASK.setupDeleteItem()
    TASK.focusForm()

  focusForm: ->
    $('#id_name').focus() if $('#id_name').length > 0
    if ('#task_item_name').length > 0
      $('#task_item_name').focus ->
        $(this).animate({ width: '+=250' })
      .blur ->
        $(this).animate({ width: '-=250' })
    return 1

  setupNewItemForm: ->
    if $('.new-task-item-form').length > 0
      csrf = PDA.getCookie('csrftoken')
      $('.csrfmiddlewaretoken').val(csrf)

      $('.new-task-item-form').submit (e) =>
        post_data = $('.new-task-item-form').serialize()
        alert "form submit called: " + post_data
        $.post('/tasks/task_item/new/', post_data, (data)=>
          alert ("(" + data.status + ") ID: " + data.record_id + ", " + data.record_name)
          if data.status == 'success'
            TASK.insertNewRecord(data.record_id, data.record_name)
          else
            TASK.flashNewItemError()
        )
        e.preventDefault()
      return 1

    return 1

  flashNewItemError: ->
    alert('Error saving new Task Item')

  insertNewRecord: (record_id, record_name) ->
    alert('New Task Item (' + record_id + ': ' + record_name + ') saved')

  setupDeleteItem: ->
    return 1

TASK.init()