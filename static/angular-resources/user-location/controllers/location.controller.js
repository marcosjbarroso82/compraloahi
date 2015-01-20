/**
 * UserLocationCtrl
 * @namespace App.location.controllers
 */
(function () {
    'use strict';

    angular
        .module('App.userLocation.controllers')
        .controller('UserLocationCtrl', UserLocationCtrl);

    UserLocationCtrl.$inject = ['$scope', 'UserLocations', 'Snackbar'];

    /**
     * @namespace UserLocationCtrl
     */
    function UserLocationCtrl($scope, UserLocations, Snackbar) {
        $scope.map = {center: {latitude: -31.4179952, longitude: -64.1890513 }, zoom: 9 };
        $scope.options = {scrollwheel: false};
        $scope.locations = {};
        $scope.location = {};

        $scope.flag_update = false;

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
            visible: true, // optional: defaults to true
            radius: 5000
        }


        UserLocations.query(function(data) {
            $scope.locations = data;
        });

        $scope.deleteLocation = function(location) {
            UserLocations.delete(location, deleteSuccess);

            function deleteSuccess(data, headers, status) {
                $scope.locations.splice($scope.locations.indexOf(location), 1);
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
            $scope.location = {};
        }

        $scope.cancelLocation = function(){
            $scope.flag_update = false;
            $scope.location = {};
        }

        $scope.addLocation = function() {
            if($scope.flag_update){
                UserLocations.update($scope.location, updateSuccess, updateError);
                $scope.flag_update = false;
            }else{
                UserLocations.save($scope.location, saveSuccess, saveError);


            }

            function saveSuccess(data, headers, status){
                Snackbar.show("Se ha agregado una ubicacion nueva");
                $scope.locations.push($scope.location);
                $scope.location = {};
            }

            function saveError(data, headers, status){
                Snackbar.show("Error al intentar agregar una nueva ubicacion");
            }

            function updateSuccess(data, headers, status){
                Snackbar.show("La ubicacion seleccionada se edito con exito");
            }

            function updateError(data, headers, status){
                Snackbar.show("Error al intentar editar la ubicacion seleccionada");
            }

        };

        /**
         * @Desc
         *
         */
        $scope.update = function(location){
            if(!$scope.flag_update){
                $scope.flag_update = true;
                $scope.location = location;
            }
        };

        $scope.select = function(location){
            $scope.location = location;
        }

    }
})();