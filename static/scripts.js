$(function() {


console.log("ok");
    if (navigator.geolocation) {
        console.log("if navigator");
        navigator.geolocation.getCurrentPosition(getCoords, getError);

    } else {
        console.log("else navigator");
        initialize( 13.30272, -87.144107);
    }


    function getCoords(position) {
        console.log("getCoords");
        var lat = position.coords.latitude;
        var lng = position.coords.longitude;

        if ($("#id_locations-0-lat").val() != "") {
            lat = $("#id_locations-0-lat").val();            
        }
        if ($("#id_locations-0-lng").val() != "") {            
            lng = $("#id_locations-0-lng").val();
        }

        initialize(lat, lng);
    }

    function getError(err) {
     console.log("getError");
        initialize( -31.428495, -64.185829);
    }

    function initialize(lat, lng) {
        console.log("initialize");
        console.log("lat:"+lat+" lng:"+lng);
        var latlng = new google.maps.LatLng(lat, lng);
        var mapSettings = {
            center: latlng,
            zoom: 9,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        }
        map = new google.maps.Map($("#mapa").get(0), mapSettings);

        var marker = new google.maps.Marker({
            position: latlng,
            map: map,
            draggable: true,
            title: "Posición"
        });
        $("#id_locations-0-title").val(marker.title);
        $("#id_locations-0-lat").val(lat);
        $("#id_locations-0-lng").val(lng);
        google.maps.event.addListener(marker, 'position_changed', function() {
            coords = marker.getPosition();
            console.log(marker.title + ": " + coords.lat() + ";" + coords.lng() );
            $("#id_locations-0-lat").val(coords.lat());
            $("#id_locations-0-lng").val(coords.lng());
        });
    }

});