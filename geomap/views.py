import json

from django.http import JsonResponse
from django.core.serializers import serialize

from .models import Region, Rent


def get_regions(request):
    regions = serialize(
        'geojson', Region.objects.all(),
        geometry_field='mpoly',
        fields=('name',)
    )
    return JsonResponse(regions, safe=False)
