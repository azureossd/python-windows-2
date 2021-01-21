from django.template import loader
from django.views import generic
from django.utils import timezone
from .models import Post

class IndexView(generic.ListView):
    template_name='blog/index.html'
    context_object_name='latest_posts'

    def get_queryset(self):
        return  Post.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'
