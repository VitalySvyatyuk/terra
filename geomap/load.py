import os

from django.contrib.gis.utils import LayerMapping

from .models import Region, Rent

region_mapping = {
    'name': 'NAME',
    'okato_code': 'OKATO_CODE',
    'area': 'AREA',
    'mpoly': 'MULTIPOLYGON'
}

rent_mapping = {
    'type': 'type',
    'num': 'num',
    'mpoint': 'MULTIPOINT'
}

region_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'test_shp_data', 'regions.shp'),
)

rent_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'test_shp_data', 'rent_points.shp'),
)


def save_to_db(model_name, shp_file, mapping):
    lm = LayerMapping(model_name, shp_file, mapping, transform=False)
    lm.save(strict=True, verbose=True)


def run():
    save_to_db(Region, region_shp, region_mapping)
    save_to_db(Rent, rent_shp, rent_mapping)
