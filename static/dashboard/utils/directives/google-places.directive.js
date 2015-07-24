/**
 * Google Places
 * @namespace dashBoardApp.util.directives
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.util.directives')
        .directive('googlePlaces', googlePlaces);

    googlePlaces.$inject = [];


    function googlePlaces() {
        return {
            restrict:'E',
            replace:true,
            // transclude:true,
            scope: {location:'=', map: '='},
            template: '<div class="input-group-custom-addon icon-addon addon-sm"><input type="text" placeholder="Ingresa tu ubicacion" name="google_places_ac" class="form-control" id="google_places_ac"> <button id="search_address_btn" class="fa fa-search" rel="tooltip" title="Busca en tu ubicacion" type="submit"></button></div>',
            link: function($scope, elm, attrs){
                var autocomplete = new google.maps.places.Autocomplete($("#google_places_ac")[0], {});
                google.maps.event.addListener(autocomplete, 'place_changed', function() {
                    var place = autocomplete.getPlace();

                    if(place.geometry){
                        $scope.location = angular.copy(place);
                        //$scope.location.lat = place.geometry.location.lat();
                        //$scope.location.lng = place.geometry.location.lng();
                        //$scope.location.center = {};
                        //$scope.location.center.latitude = place.geometry.location.lat();
                        //$scope.location.center.longitude = place.geometry.location.lng();

                        //$scope.map.center.latitude = angular.copy(place.geometry.location.A);
                        //$scope.map.center.longitude = angular.copy(place.geometry.location.F);

                        $scope.$apply();
                    }

                });
            }
        };

    }
})();