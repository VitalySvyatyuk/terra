from django.urls import path
from django.views.generic import TemplateView

from .models import Region
from .views import RegionView

urlpatterns = [
    path('', TemplateView.as_view(template_name='geomap/geomap.html')),
    path('get_regions.geojson', RegionView.as_view(model=Region)),
]
