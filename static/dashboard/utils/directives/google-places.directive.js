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
            template: '<div class="input-group"><input id="google_places_ac" name="google_places_ac" type="text" class="input-block-level form-control"/><span class="input-group-addon"><i class="glyphicon glyphicon-search"></i></span>',
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