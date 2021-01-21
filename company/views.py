from django.views import generic
from django.utils import timezone

class HomePageView(generic.TemplateView):
    template_name = 'site/home.html'