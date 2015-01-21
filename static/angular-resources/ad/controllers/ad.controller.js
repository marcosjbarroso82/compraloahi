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
        $scope.next_page = null;
        $scope.prev_page = null;
        $scope.count_page = 0;
        $scope.current_page = 1;
        $scope.pages = [];

        $scope.map = {
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
                console.log("cargando datos");
                $scope.ads = data.results;

                $scope.next_page = data.next;
                $scope.prev_page = data.previous;

                // set Circle style for each ad
                $.each($scope.ads,function(index, ad){
                    setCircleStyle(ad);

                });
            });
        }

        $scope.selectAd = function (ad) {
            ad.selected = true;
            setCircleStyle(ad);
        }
        $scope.deselectAd = function (ad) {
            ad.selected = false;
            setCircleStyle(ad);
        }

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