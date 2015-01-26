/**
 * AdCtrl
 * @namespace App.ad.controllers
 */

(function () {
    'use strict';

    angular
        .module('App.ad.controllers')
        .controller('AdCtrl', AdCtrl);

    AdCtrl.$inject = ['$scope', 'Ad'];

    /**
     * @namespace AdCtrl
     */
    function AdCtrl($scope, Ad) {
        $scope.ads = {};

        $scope.search_location = search_location;
        $scope.search_location.changed = false;
        $scope.search_location.stroke = {color: '#009900', weight: 2, opacity: 0.1 };
        $scope.search_location.fill = {color: '#009900', weight: 2, opacity: 0.1 };

        $scope.user_locations = user_locations;
        $scope.user_location_selected = {};

        $scope.existsLocationTitle = function (title) {
            for (var i=0; i < $scope.user_locations.length; i++) {
                if ($scope.user_locations[i].title === $scope.search_location.title) {
                    return true;
                }
            }
            return false;
        }

        $scope.submitNewLocation= function () {
            // TODO: How about validating the others fields?
            if ($scope.search_location.title && !$scope.existsLocationTitle($scope.search_location.title) ) {
                $.post("/api/v1/user-locations/",
                    {
                        title: $scope.search_location.title,
                        lat: $scope.search_location.location.latitude,
                        lng: $scope.search_location.location.longitude,
                        radius: $scope.search_location.radius,
                        csrfmiddlewaretoken: csrf
                    },
                    function(data) {
                        $scope.user_locations.push({
                            latitude: data.lat,
                            longitude: data.lng,
                            radius: data.radius,
                            pk: data.id,
                            title: data.title
                        });
                        $('#modalNewLocation').modal('hide');

                        $scope.user_location_selected = {};

                        // TODO: this should select the option in the html selct. Bu it's not working
                        $scope.$apply(function(){
                            // TODO: It would be better to use some kind of id
                            $('#user-locations-select option[label="'+ data.title +'"]').attr("selected", "selected");
                        });

                        $scope.search_location.changed = false;
                        $scope.search_location.title= "";
                        $("#search_location_name").val("");


                    })
                    .fail(function(){
                        $('#modalNewLocation .modal-body').html("Ocurrio un error al guardar su ubicación");
                    });
            } else {
                // TODO: manage this in a better way
                window.alert("Ingrese un nombre que no exista ya");
            }


        }

        $scope.$watch('user_location_selected',function(val,old){
            //  this IF makes sure the code is no executed right when its loaded
            if ($scope.user_location_selected.latitude
                && $scope.user_location_selected.longitude
                && $scope.user_location_selected.radius) {

                $scope.search_location.location.latitude = $scope.user_location_selected.latitude;
                $scope.search_location.location.longitude = $scope.user_location_selected.longitude;
                $scope.search_location.radius = $scope.user_location_selected.radius;
                $scope.search_location.changed = false;
            }
        });

        // This watch is for range input which returns text instead of number
        $scope.$watch('search_location.radius',function(val,old){
            $scope.search_location.radius = parseInt(val);
            if ($scope.search_location.radius != $scope.user_location_selected.radius
                && $scope.search_location.changed != true) {
                // TODO: este evento se esta llamando dos veces por problemas de formato de entero y flotante en el radio
                searchLocationChanged();
            }
        });

        $scope.$watch('search_location.location.latitude',function(val,old){
            if ($scope.search_location.location.latitude != $scope.user_location_selected.latitude
                && $scope.search_location.changed!=true) {
                searchLocationChanged();
            }
        });
        $scope.$watch('search_location.location.longitude',function(val,old){
            if ($scope.search_location.location.longitude != $scope.user_location_selected.longitude
                && $scope.search_location.changed!=true) {
                searchLocationChanged();
            }
        });

        $scope.map = {
            // TODO: define a proper location initialization
            center: {latitude: -31.4179952,
                longitude: -64.1890513 }, zoom: 9,
            options: {},
            control: {},
            circle_events: {
                click: function (marker, eventName, args) {
                    $('html, body').animate({
                        scrollTop: $("#ad-anchor-" + args.$parent.ad.pk).offset().top - 70
                    }, 1000);
                },
                mouseover: function (marker, eventName, args) {
                    args.$parent.ad.selected = true;
                },
                mouseout: function (marker, eventName, args) {
                    args.$parent.ad.selected = false;
                }
            }
        };

        $scope.location_options = {
            draggable: false, // optional: defaults to false
            clickable: true, // optional: defaults to true
            editable: false, // optional: defaults to false
            visible: true // optional: defaults to true
        }

        getAds();

        function getAds(){
            Ad.get(function(data) {
                $scope.ads = data.results;

                $scope.next_page = data.next;
                $scope.prev_page = data.previous;

                // set Circle style for each ad
                $.each($scope.ads,function(index, ad){
                    setCircleStyle(ad);

                });
            });
        }

        function searchLocationChanged() {
            if (typeof $scope.user_location_selected.latitude !== search_location.location.latitude
                && typeof $scope.user_location_selected.longitude !== search_location.location.longitude
                && typeof $scope.user_location_selected.radius !== search_location.location.radius ){
                $scope.search_location.changed = true;
                $scope.user_location_selected = {};
            }
        }

        $scope.selectAd = function (ad) {
            ad.selected = true;
            setCircleStyle(ad);
        }
        $scope.deselectAd = function (ad) {
            ad.selected = false;
            setCircleStyle(ad);
        }

        // TODO: Implement this functionality
        $scope.AddToFavourites = function(ad) {
            window.alert("NOT IMLPEMENTED YET! ad" + ad.pk + " should be added to favourites")
        }

        $scope.centerMap = function(position) {
            $scope.map.control.getGMap().panTo(new google.maps.LatLng(position.latitude, position.longitude));
        }

        function setCircleStyle(ad){
            if (ad.selected) {
                ad.stroke = {color: '#00FF00', weight: 2, opacity: 1 };
                ad.fill = {color: '#00AA00', weight: 2, opacity: 1 };
            } else {
                ad.stroke = {color: '#FF0000', weight: 2, opacity: 1 };
                ad.fill = {color: '#AA0000', weight: 2, opacity: 1 };
            }
        }

        $scope.circle_events = {
            click: function (marker, eventName, args) {
                $('html, body').animate({
                    scrollTop: $("#ad-anchor-" + args.$parent.ad.pk).offset().top - 70
                }, 1000);
            },
            mouseover: function (marker, eventName, args) {
                args.$parent.ad.selected = true;
            },
            mouseout: function (marker, eventName, args) {
                args.$parent.ad.selected = false;
            }
        };
    }
})();