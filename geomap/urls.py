from django.urls import path
from django.views.generic import TemplateView

from .views import get_regions

urlpatterns = [
    path('', TemplateView.as_view(template_name='geomap/geomap.html')),
    path('get_regions/', get_regions, name='get_regions'),
]
