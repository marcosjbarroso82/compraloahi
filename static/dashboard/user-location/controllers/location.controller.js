/**
 * UserLocationCtrl
 * @namespace dashBoardApp.location.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.userLocation.controllers')
        .controller('UserLocationCtrl', UserLocationCtrl);

    UserLocationCtrl.$inject = ['$scope', 'UserLocations', 'Snackbar'];

    /**
     * @namespace UserLocationCtrl
     */
    function UserLocationCtrl($scope, UserLocations, Snackbar) {
        // TODO: provide a proper map center location
        $scope.map = {center: {latitude: -31.4179952, longitude: -64.1890513 }, zoom: 9 };
        $scope.options = {scrollwheel: false};
        $scope.locations = {};
        $scope.location = {};

        $scope.flag_update = false;
        $scope.flag_create = false;

        $scope.location_options = {
            stroke: {
                color: '#08B21F',
                weight: 2,
                opacity: 1
            },
            fill: {
                color: '#08B21F',
                opacity: 0.5
            },
            geodesic: true, // optional: defaults to false
            draggable: true, // optional: defaults to false
            clickable: true, // optional: defaults to true
            editable: true, // optional: defaults to false
            visible: true // optional: defaults to true
        }

        $scope.hideLocations = function () {
            for (var i=0; i < $scope.locations.length; i++) {
                $scope.locations[i].visible = false;
            }
        }

        $scope.resetLocations = function () {
            // clean search places text box
            $('#google_places_ac').val('');
            // if a location wa being updated, set to original values
            if ($scope.flag_update) {
                console.log($scope.location);
                $scope.location.center.latitude = $scope.location.lat_original;
                $scope.location.center.longitude = $scope.location.lng_original;
                $scope.location.radius = $scope.location.radius_original;
            }
            $scope.location = {};
            $scope.flag_create = false;
            $scope.flag_update = false;
            for (var i=0; i < $scope.locations.length; i++) {
                $scope.locations[i].visible = true;
                $scope.locations[i].draggable = false;
                $scope.locations[i].editable = false;
            }
        }

        UserLocations.query(function(data) {
            $scope.locations = data;
            $scope.resetLocations();
        });

        $scope.deleteLocation = function(location) {
            $scope.resetLocations();
            UserLocations.delete(location, deleteSuccess, deleteError);

            function deleteSuccess(data, headers, status) {
                $scope.locations.splice($scope.locations.indexOf(location), 1);
            }
            function deleteError(data, headers, status){
                Snackbar.show("Error al intentar borrar la ubicacion seleccionada");
            }
        }

        $scope.doSearch = function(){
            if($scope.location === ''){
                alert('Directive did not update the location property in parent controller.');
            } else {
                console.log($scope.location);
            }
        };

        $scope.newLocation = function(){
            $scope.flag_create = true;
            $scope.hideLocations();
            $scope.location = {radius: 10000, center: {}};
            $scope.location.center.latitude = $scope.map.center.latitude;
            $scope.location.center.longitude = $scope.map.center.longitude;
            $scope.location.visible = true;
            $scope.location.draggable = true;
            $scope.location.editable = true;
        }

        $scope.cancelLocation = function(){
            $scope.resetLocations();

        }

        $scope.addLocation = function() {
            if($scope.flag_update){
                $scope.location.lat = $scope.location.center.latitude;
                $scope.location.lng = $scope.location.center.longitude;
                UserLocations.update($scope.location, updateSuccess, updateError);
            }else if($scope.flag_create){
                UserLocations.save($scope.location, saveSuccess, saveError);
            }

            function saveSuccess(data, headers, status){
                Snackbar.show("Se ha agregado una ubicacion nueva");
                $scope.location.id = data.id;
                $scope.locations.push($scope.location);
                $scope.location = {};
                $scope.resetLocations();
            }

            function saveError(data, headers, status){
                Snackbar.show("Error al intentar agregar una nueva ubicacion");
                $scope.resetLocations();
            }

            function updateSuccess(data, headers, status){
                Snackbar.show("La ubicacion seleccionada se edito con exito");
                $scope.flag_update = false;
                $scope.resetLocations();
            }

            function updateError(data, headers, status){
                Snackbar.show("Error al intentar editar la ubicacion seleccionada");
                $scope.resetLocations();
            }
        };

        /**
         * @Desc
         *
         */
        $scope.update = function(location){
            $scope.resetLocations();
            $scope.hideLocations();
            console.log(location);
            location.lat_original = location.lat;
            location.lng_original = location.lng;
            location.radius_original = location.radius;
            $scope.location = location;
            $scope.map.center.latitude = $scope.location.center.latitude;
            $scope.map.center.longitude = $scope.location.center.longitude;
            location.draggable = true;
            location.editable = true;
            location.visible = true;
            $scope.flag_update = true;
        };

        $scope.select = function(location){
            $scope.location = location;
        }

    }
})();