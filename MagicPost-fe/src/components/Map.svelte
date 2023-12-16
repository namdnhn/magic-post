<script lang="js">
   goongjs.accessToken = 'g63Co8g8U7R5KYoHAwM5lpuNBQscNliR5WMayCHK';
var map = new goongjs.Map({
container: 'map',
style: 'https://tiles.goong.io/assets/goong_map_web.json',
center: [105.80278, 20.99245],
zoom: 10 	
});
console.log(map + "map");
 
map.on('load', function () {
var layers = map.getStyle().layers;
// Find the index of the first symbol layer in the map style
var firstSymbolId;
for (var i = 0; i < layers.length; i++) {
if (layers[i].type === 'symbol') {
firstSymbolId = layers[i].id;
break;
}
}
// Initialize goongClient with an API KEY
var goongClient = goongSdk({
accessToken: '0i1kR7eZhM4SBTMSyoRS1QIBwwCVaZFGej3LM67y'
});
// Get Directions
goongClient.directions
.getDirections({
origin: '21.013732756308617, 105.82102601014938',
destination: '20.43020737480039, 106.16145856965633',
vehicle: 'car'
})
.send()
.then(function (response) {
var directions = response.body;
var route = directions.routes[0];
 
var geometry_string = route.overview_polyline.points;
var geoJSON = polyline.toGeoJSON(geometry_string);
map.addSource('route', {
'type': 'geojson',
'data': geoJSON
});
// Add route layer below symbol layers
map.addLayer(
{
'id': 'route',
'type': 'line',
'source': 'route',
'layout': {
'line-join': 'round',
'line-cap': 'round'
},
'paint': {
'line-color': '#1e88e5',
'line-width': 8
}
},
firstSymbolId
);
});
});
</script>