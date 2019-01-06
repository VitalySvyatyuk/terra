var geomap = L.map('geomap').setView([49.4, 44.0], 7);

L.Util.ajax("get_regions").then(function(data) {
    L.geoJSON(JSON.parse(data)).addTo(geomap);
});