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

    /**
     * @namespace googlePlaces
     */
    function googlePlaces() {
        /**
         * @name directive
         * @desc The directive to be returned
         * @memberOf dashBoardApp.util.directives.googlePlaces
         */
        return {
            restrict:'E',
            replace:true,
            // transclude:true,
            scope: {location:'=', map: '='},
            template: '<div class="input-group-custom-addon icon-addon addon-sm"><input type="text" placeholder="Ingresa tu ubicacion" name="google_places_ac" class="form-control" id="google_places_ac"> <button id="search_address_btn" class="glyphicon glyphicon-search" rel="tooltip" title="Busca en tu ubicacion" type="submit"></button></div>',
            link: function($scope, elm, attrs){
                var autocomplete = new google.maps.places.Autocomplete($("#google_places_ac")[0], {});
                google.maps.event.addListener(autocomplete, 'place_changed', function() {
                    var place = autocomplete.getPlace();
                    //$scope.location = place.geometry.location.lat() + ',' + place.geometry.location.lng();
                    $scope.location.lat = place.geometry.location.lat();
                    $scope.location.lng = place.geometry.location.lng();
                    $scope.location.center = {};
                    $scope.location.center.latitude = place.geometry.location.lat();
                    $scope.location.center.longitude = place.geometry.location.lng();

                    $scope.map.center.latitude = $scope.location.center.latitude;
                    $scope.map.center.longitude = $scope.location.center.longitude;

                    $scope.$apply();
                });
            }
        };

    }
})();