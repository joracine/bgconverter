from django.contrib import admin
from django.urls import path

from bgconverter.views import converter

urlpatterns = [
    path(r'bgconverter/', converter.ConverterView.as_view(), name='converter'),

    # AJAX Handlers
    path(r'bgconverter/converters/mmol_per_l_to_mg_per_dl/', converter.convert_mmol_per_l_to_mg_per_dl_view,
         name='convert_mmol_per_l_to_mg_per_dl'),
    path(r'bgconverter/converters/mg_per_dl_to_mmol_per_l/', converter.convert_mg_per_dl_to_mmol_per_l_view,
         name='convert_mg_per_dl_to_mmol_per_l'),

    path(r'bgconverter/admin/', admin.site.urls),
]
