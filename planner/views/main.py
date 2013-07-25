from django.views.generic import TemplateView


class MainPlannerView(TemplateView):
  template_name = 'planner/index.html'
  # form_class = SearchTagForm
