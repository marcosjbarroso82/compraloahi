/* Directives */
angular.module('OtdDirectives', []).
    directive('googlePlaces', function(){
        return {
            restrict:'E',
            replace:true,
            // transclude:true,
            scope: {location:'='},
            template: '<input id="google_places_ac" name="google_places_ac" type="text" class="input-block-level"/>',
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

                    $scope.$apply();
                });
            }
        }
    });
