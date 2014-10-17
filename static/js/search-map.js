var current_lat;
var current_lng;
var position_marker;
var map;

$(function() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(getCoords, getError);

    } else {
        // TODO: Set to a proper Location
        current_lat = -31.428495;
        current_lng = -64.185829;
        initialize();
    }
});

function getCoords(position) {
    console.log("getCoords");
    current_lat = position.coords.latitude;
    current_lng = position.coords.longitude;
    initialize();
}

function getError(err) {
    console.log("getError");
    // TODO: Set to a proper Location
    current_lat = -31.428495;
    current_lng = -64.185829;
    initialize();
}

function initialize() {
    console.log("initialize()");
    console.log("current_lat: " + current_lat + " current_lng: " + current_lng);
    var latlng = new google.maps.LatLng(current_lat, current_lng);
    var mapSettings = {
        center: latlng,
        zoom: 12,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    }
    map = new google.maps.Map($("#mapa").get(0), mapSettings);

    position_marker = new google.maps.Marker({
        position: latlng,
        map: map,
        draggable: true,
        title: "Posición"
    });
    linkMapToSearchForm();
}

function linkMapToSearchForm() {
    console.log("linkMapToSearchForm()");
    console.log("current_lat: " + current_lat + " current_lng: " + current_lng);
    $("#lat").val(current_lat);
    $("#lng").val(current_lat);

    google.maps.event.addListener(position_marker, 'position_changed', function() {
        coords = position_marker.getPosition();
        console.log( coords.lat() + ";" + coords.lng() );
        $("#lat").val(coords.lat());
        $("#lng").val(coords.lng());
    });

}