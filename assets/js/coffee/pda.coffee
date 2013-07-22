PDA =
  init: ->
    PDA.showMessages()
    PDA.initializeDelete()

  initializeDelete: ->
    deletes = $('.delete-record')
    if deletes.length > 0
      csrf = PDA.getCookie('csrftoken')
      PDA.insertDeleteForm(csrf)
      deletes.each (i, elem) =>
        $(elem).click =>
          if confirm('Are you sure you want to delete this record?')
            $('#delete_form').attr('action', $(elem).attr('data'));
            $('#delete_form').submit()

  showMessages: ->
    if $('.messages').length > 0
      msgBox = $('.messages')

      left = PDA.getWindowQuarter(msgBox)
      msgBox.css('left', left + 'px')
      .fadeIn(1000)
      .animate('top': '45px')
      .bind 'click', (event) =>
        msgBox.fadeOut()

  insertDeleteForm: (csrf) ->
    $('body').append('
      <form id="delete_form" name="delete_form" action="" method="post" class="delete-form">
        <input type="hidden" name="csrfmiddlewaretoken" value="' + csrf + '" />
      </form>
    ')

  getWindowCenter: (e) ->
    (($(window).width() - e.width()) / 2)

  getWindowQuarter: (e) ->
    (($(window).width() - e.width()) / 4) * 3

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

PDA.init()