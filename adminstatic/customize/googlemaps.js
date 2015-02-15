var map;
function initialize() {
	var xielab = new google.maps.LatLng(42.3772437,-71.1157683);
	var mapOptions = {
		zoom: 16,
		center: xielab
	};
	map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

	var marker = new google.maps.Marker({
		position: xielab,
		map: map,
		title: "Xie Group"
	});
	
	var contentString = "<div class='infocontent'><h5>Xie Group</h5>" +
		"Harvard University<br>" +
		"Department of Chemistry &amp; Chemical Biology<br>" +
		"12 Oxford Street<br>" +
		"Cambridge, MA 02138<br></div>";

	var infowindow = new google.maps.InfoWindow({
		content: contentString,
	});

	google.maps.event.addListener(marker, 'click', function() {
		infowindow.open(map, marker);
	});
}

google.maps.event.addDomListener(window, 'load', initialize);
