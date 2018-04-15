from django.views import generic

class BGConverterView(generic.TemplateView):
    template_name = 'bgconverter/index.html'
