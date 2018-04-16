from django.http import JsonResponse
from django.views import generic


class ConverterView(generic.TemplateView):
    template_name = 'bgconverter/converter.html'

def convert_mmol_per_l_to_mg_per_dl_view(request):
    mmol_per_l = float(request.GET.get('mmol_per_l', 0.0))
    data = {
        'mg_per_dl': str(convert_mmol_per_l_to_mg_per_dl(mmol_per_l))
    }
    return JsonResponse(data)

def convert_mg_per_dl_to_mmol_per_l_view(request):
    mg_per_dl = float(request.GET.get('mg_per_dl', 0.0))
    data = {
        'mmol_per_l': str(convert_mg_per_dl_to_mmol_per_l(mg_per_dl))
    }
    return JsonResponse(data)

def convert_mmol_per_l_to_mg_per_dl(mmol_per_l):
    return float(mmol_per_l) / 18.0

def convert_mg_per_dl_to_mmol_per_l(mg_per_dl):
    return float(mg_per_dl) * 18.0
