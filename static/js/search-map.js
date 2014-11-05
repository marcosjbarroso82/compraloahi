var current_lat;
var current_lng;
var current_radius = 1000;
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
        zoom: 9,
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

    loadPositions(json_data.results);
}

function clearMapPositions() {
    console.log('clearMapPositions');
    ad_position_areas.forEach(function(adPositionArea) {
        /* console.log(adPositionArea); */
        adPositionArea.setMap(null);
    });
    /*
     for (var i=0; i < ad_position_areas.length; i++) {
         console.log('ad_position_areas ' + i + ':' + ad_position_areas[i]);
         ad_position_areas[i][0].setMap(null);
    }
    */
}

function loadPositions(positions) {
    console.log("loadPositions");

    ad_position_areas = [];
    /* console.log(positions); */
    for (var i=0; i < positions.length; i++) {
        var position = positions[i];
        ad_position_areas[position.pk] = new google.maps.Circle({
            content: "contenido",
            name: "este es el nombre",
            pk: position.pk,
            map: map,
            center: new google.maps.LatLng(position.lat, position.lng),
            radius: 3000,
            strokeColor:"#0000FF",
        strokeOpacity:0.8,
        strokeWeight:2,
        fillColor:"#0000FF",
        fillOpacity:0.4
        });

        // escucha a las posiciones
        google.maps.event.addListener(ad_position_areas[position.pk],'mouseover',function(pk){
            $('li[data-pk="'+ this.pk +'"]').css('background-color', '#f0f');
        });
        google.maps.event.addListener(ad_position_areas[position.pk],'mouseout',function(pk){
            $('li[data-pk="'+ this.pk +'"]').css('background-color', '#fff');

        });

        google.maps.event.addListener(ad_position_areas[position.pk], 'click', function(event) {
            $('li[data-pk="'+ this.pk +'"]').css('background-color', '#f0f');

              $('html, body').animate({
                scrollTop: $("#" + "ad-anchor-" + this.pk).offset().top - 70
            }, 1000);

        });
    }
}

function linkMapToSearchForm() {
    console.log("linkMapToSearchForm()");
    console.log("current_lat: " + current_lat + " current_lng: " + current_lng);
    $("#lat").val(current_lat);
    $("#lng").val(current_lng);
    $("#radius").val( current_radius );

    google.maps.event.addListener(position_area, 'center_changed', function() {
        /* console.log('center: ' + position_area.center.lat() + ";" + position_area.center.lng() ); */
        $("#lat").val( position_area.center.lat() );
        $("#lng").val( position_area.center.lng() );
    });

    google.maps.event.addListener(position_area, 'radius_changed', function() {
        //console.log('radius: ' + position_area.getRadius());
        current_radius = position_area.getRadius();
        $("#radius").val( current_radius );
    });

    $("#radius").change(function(){
        console.log("cambiando radio en el mapa");
    position_area.setRadius(Number($("#radius").val()));
    });


}