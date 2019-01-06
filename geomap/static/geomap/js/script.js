var geomap = L.map('geomap').setView([49.4, 44.0], 7);

L.Util.ajax('get_regions.geojson').then(function(data) {
    var geojsonJayer = L.geoJSON(data, {
        onEachFeature: function(feature, layer) {
            var stats = '';
            for (var point in feature.properties.points) {
                stats += '<p class="popup-text">- ' + point + ': '
                    + feature.properties.point_nums[point]
                    + ' т, ' + feature.properties.points[point]
                    + ' шт</p>'
            }
            layer.bindPopup(
                '<p class="popup-text">' + feature.properties.name + ':</p>' + stats
            );
            layer.on('mouseover', function() {
                this.setStyle({
                    color: '#169547',
                    fillOpacity: 0.5
                })
            });
            layer.on('mouseout', function(e) {
                geojsonJayer.resetStyle(e.target)
            });
        }
    }).addTo(geomap);
});
