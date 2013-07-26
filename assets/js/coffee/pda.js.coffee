window.PDA =
  # Constructor / Initializer function
  init: ->
    PDA.showMessages()
    PDA.initializeDelete()
    PDA.initializeForms()

  # Sets up the delete functionality for index pages.
  initializeDelete: ->
    deletes = $('.delete-record')
    if deletes.length > 0
      csrf = PDA.getCookie('csrftoken')
      PDA.insertDeleteForm(csrf)
      deletes.each (i, element) =>
        $(element).click =>
          if confirm('Are you sure you want to delete this record?')
            $('#delete_form').attr('action', $(element).attr('data'));
            $('#delete_form').submit()

  initializeForms: ->
    $('.datetimeinput').datetimepicker({dateFormat: 'yy-mm-dd'});

  # Shows the messages div if flash message has been passed.
  showMessages: ->
    if $('.messages').length > 0
      msgBox = $('.messages')

      left = PDA.getWindowQuarter(msgBox)
      msgBox.css('left', left + 'px')
      .fadeIn(1000)
      .animate('top': '45px')
      .bind 'click', (event) =>
        msgBox.fadeOut()


  # HTML Insert Functions #####

  # Appends an empty form (except for hidden csrf token) for submitting delete requests.
  insertDeleteForm: (csrf) ->
    $('body').append('
      <form id="delete_form" name="delete_form" action="" method="post" class="delete-form">
        <input type="hidden" name="csrfmiddlewaretoken" value="' + csrf + '" />
      </form>
    ')


  # Getter functions #####


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