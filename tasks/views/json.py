from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect


@login_required
@csrf_protect
def create_task_item(request):
    pass


@login_required
@csrf_protect
def delete_task_item(request):
    pass

