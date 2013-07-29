from datetime import datetime, date, time

from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

# Decorators
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
# For JSON Handling
from django.core import serializers
from django.utils import simplejson

from ..models import TaskItem


@login_required
@csrf_protect
def create_task_item(request):
  if request.method == 'POST':
    try:
      task_id = request.POST.get('task_id')
      name = request.POST.get('name')
      if task_id == '' and name == '':
        raise Exception('Incomplete form submitted')
      record = TaskItem()
      record.task_id = int(task_id)
      record.owner_id = request.user.id
      record.name = name
      record.completed = False
      record.created_at = datetime.now()
      record.created_at = datetime.now()
      record.save()
      status = 'success'
      record_id = record.id
      record_name = record.name
    except:
      status = 'fail'
      record_id = None
      record_name = None

    raw = {
      'status': status,
      'task_id': task_id,
      'record_id': record_id,
      'record_name': record_name
    }
    data = simplejson.dumps(raw)
    return HttpResponse(data, mimetype='application/json')
  else:
    return HttpResponseRedirect(reverse('tasks_main'))


@login_required
@csrf_protect
def update_task_item(request):
  pass


@login_required
@csrf_protect
def delete_task_item(request):
    pass


