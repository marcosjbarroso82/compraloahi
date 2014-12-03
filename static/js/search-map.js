var current_lat;
var current_lng;
var current_radius = parseFloat(getParameterByName('radius') !== '' ? getParameterByName('radius') : 1000);
var q = getParameterByName('q') !== '' ? getParameterByName('q') : '';

var position_area;
var map;
var ad_position_areas = [];


var map_bounds = new google.maps.LatLngBounds();


$(function() {
    // Get Lat and Lng from url
    if (getParameterByName('lat') !== '' && getParameterByName('lng') !== '') {
        current_lat = getParameterByName('lat');
        current_lng = getParameterByName('lng');
        initialize();
    } else {
        // obtener ubicacion a travez de sensor u otro medio
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(getCoords, getError);
        }
        // si no logramos obtener la ubicacion, poner una x defecto
        else {
            // TODO: Set to a proper Location
            current_lat = -31.428495;
            current_lng = -64.185829;
            initialize();
        }
    }
});
function getCoords(position) {
    current_lat = position.coords.latitude;
    current_lng = position.coords.longitude;
    initialize();
}

function getError(err) {
    // TODO: Set to a proper Location
    current_lat = -31.428495;
    current_lng = -64.185829;
    initialize();
}

function initialize() {
    $("#lat").val(current_lat);

    $("#lng").val(current_lng);
    if(current_radius == ''){
        current_radius = 1000;
    }
    $("#radius").val( current_radius );
    $("#range").html(parseInt(current_radius));


    $("#q").val(q);

    var latlng = new google.maps.LatLng(current_lat, current_lng);

    map_bounds.extend(latlng);

    var mapSettings = {
        center: latlng,
        zoom: 12,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    }

    map = new google.maps.Map($("#mapa").get(0), mapSettings);
    position_area = new google.maps.Circle({
        map: map,
        editable: true,
        center:latlng,
        radius:current_radius,
        strokeColor:"#0000FF",
        strokeOpacity:0.8,
        strokeWeight:2,
        fillColor:"#0000FF",
        fillOpacity:0.4,
        zIndex: 10
    });

    linkMapToSearchForm();


    loadPosition();
}

function clearMapPositions() {
    ad_position_areas.forEach(function(adPositionArea) {
        adPositionArea.setMap(null);
    });
}


function linkMapToSearchForm() {


    google.maps.event.addListener(position_area, 'center_changed', function() {
        $("#lat").val( position_area.center.lat() );
        $("#lng").val( position_area.center.lng() );
    });
    google.maps.event.addListener(position_area, 'radius_changed', function() {
        current_radius = position_area.getRadius();
        if(parseInt(current_radius) > 600000){
            position_area.setRadius(600000);
        }
        $("#radius").val( current_radius );
        $("#range").html(parseInt(current_radius));
        $("#map_radius").val(current_radius);
    });

    // TODO: Quizas on key pressed event funcionaria mejor. Mas en timepo real
    $("#radius").change(function(){
        current_radius = Number($("#radius").val());
        position_area.setRadius(current_radius);
        $("#map_radius").val(current_radius);
    });


    $("#map_radius").change(function(){
        current_radius = Number($("#map_radius").val());
        position_area.setRadius(current_radius);
        $("#radius").val(current_radius);
    });
}


function loadPosition(){
    //Array de avisos
    var ads_list = $("#ads-list").children();

    ads_list.each(function(){
        var ad_id = $(this)[0].getAttribute('data_pk');
        var lat = $(this).find('.lat')[0].innerHTML;
        var lng = $(this).find('.lng')[0].innerHTML;
        var latLng = new google.maps.LatLng(lat, lng);

        map_bounds.extend(latLng);

        ad_position_areas[ad_id] = new google.maps.Circle({
            content: "contenido",
            name: "este es el nombre",
            pk: ad_id,
            map: map,
            center: latLng,
            radius: 500,
            strokeColor:"green",
            strokeOpacity:0.8,
            strokeWeight:2,
            fillColor:"green",
            fillOpacity:0.4,
            zIndex: 11
        });

        // escucha a las posiciones
        google.maps.event.addListener(ad_position_areas[ad_id],'mouseover',function(pk){
            $('li[data_pk="'+ this.pk +'"]').css('background-color', '#8686DE');
        });
        google.maps.event.addListener(ad_position_areas[ad_id],'mouseout',function(pk){
            $('li[data_pk="'+ this.pk +'"]').css('background-color', '#fff');

        });

        google.maps.event.addListener(ad_position_areas[ad_id], 'click', function(event) {
            $('li[data_pk="'+ ad_id +'"]').css('background-color', '#8686DE');

              $('html, body').animate({
                scrollTop: $("#ad-anchor-" + ad_id).offset().top - 70
            }, 1000);

        });


         // Agrega funciones al evento hover
         $( this ).hover(
         function(){
         ad_position_areas[ad_id].setMap(map);
         ad_position_areas[ad_id].setOptions({strokeWeight: 2.0, fillColor: 'red'});
         },
         function(){
         ad_position_areas[ad_id].setOptions({strokeWeight: 2.0, fillColor: 'green'});
         })

         });

    map.fitBounds(map_bounds);
}


function getParameterByName(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}