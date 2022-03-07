from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from viewer.models import ThreeD


class HomeView(TemplateView):

    template_name = 'home.html'
    http_method_names = ['get']

    def get(self, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        three_d_models = ThreeD.objects.order_by('-id')
        context.update({"three_d_models": three_d_models})
        return self.render_to_response(context)
