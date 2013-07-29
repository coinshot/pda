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
        $.post('/tasks/task_item/new/', post_data, (data)=>
          $('#task_item_name').val('')
          if data.status == 'success'
            TASK.insertNewRecord(data.task_id, data.record_id, data.record_name)
          else
            TASK.flashNewItemError()
        )
        e.preventDefault()
      return 1

    return 1

  flashNewItemError: ->
    alert('Error saving new Task Item')

  insertNewRecord: (task_id, record_id, record_name) ->
    html = '
    <div class="record-row">
      <a href="/tasks/' + task_id + '/task_items/edit/' + record_id + '">' + record_name + '</a>
      <span class="record-controls">
      <a class="delete-record" data="/tasks/task_item/delete/' + record_id + '" href="#">Delete</a>
      </span>
    </div>
    '
    $('.task-records-list').append(html)

  setupDeleteItem: ->
    return 1

TASK.init()