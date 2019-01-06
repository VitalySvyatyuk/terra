from djgeojson.views import GeoJSONLayerView


class RegionView(GeoJSONLayerView):
    properties = ('name', 'point_nums', 'points',)
    geometry_field = 'mpoly'
