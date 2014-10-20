var current_lat;
var current_lng;
var current_radius = 10000;
var position_marker;
var position_area;
var map;
var ad_position_areas = [];

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
    /*
    position_marker = new google.maps.Marker({
        position: latlng,
        map: map,
        draggable: true,
        title: "Posición"
    });
    */
    position_area = new google.maps.Circle({
        map: map,
        editable: true,
        center:latlng,
        radius:current_radius,
        strokeColor:"#0000FF",
        strokeOpacity:0.8,
        strokeWeight:2,
        fillColor:"#0000FF",
        fillOpacity:0.4
    });

    linkMapToSearchForm();
}

function loadPositions(positions) {
    ad_position_areas = []
    for (var i=0; i < positions.length; i++) {
        position = positions[i];
        ad_position_areas[position.pk] = new google.maps.Circle({map: map,
            center: new google.maps.LatLng(position.lat, position.lng), radius: 300});
    }
    //ad_position_areas[$("#list").children()[0].dataset.pk].setMap(map)

}

function linkMapToSearchForm() {
    console.log("linkMapToSearchForm()");
    console.log("current_lat: " + current_lat + " current_lng: " + current_lng);
    $("#lat").val(current_lat);
    $("#lng").val(current_lat);
    $("#radius").val( current_radius );
    /*
    google.maps.event.addListener(position_marker, 'position_changed', function() {
        coords = position_marker.getPosition();
        //console.log( coords.lat() + ";" + coords.lng() );
        //$("#lat").val(coords.lat());
        //$("#lng").val(coords.lng());
    });
    */
    google.maps.event.addListener(position_area, 'center_changed', function() {
        console.log('center: ' + position_area.center.lat() + ";" + position_area.center.lng() );
        $("#lat").val( position_area.center.lat() );
        $("#lng").val( position_area.center.lng() );
    });

    google.maps.event.addListener(position_area, 'radius_changed', function() {
        //console.log('radius: ' + position_area.getRadius());
        current_radius = position_area.getRadius();
        $("#radius").val( current_radius );
    });

}