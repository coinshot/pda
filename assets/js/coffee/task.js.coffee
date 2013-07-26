window.TASK =
  init: ->
    TASK.prepareNewItemForm()
    TASK.focusForm()

  focusForm: ->
    $('#id_name').focus() if $('#id_name').length > 0

  prepareNewItemForm: ->
    csrf = PDA.getCookie('csrftoken')
    $('.csrfmiddlewaretoken').val(csrf)

  getCookie: (name) ->
    cookieValue = null
    if (document.cookie && document.cookie != '')
      cookies = document.cookie.split(';')
      for c in cookies
        cookie = jQuery.trim(c)
        if cookie.substring(0, name.length + 1) == (name + '=')
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
          break
    return cookieValue

TASK.init()