/**
 * UserLocationCtrl
 * @namespace dashBoardApp.location.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.userLocation.controllers')
        .controller('UserLocationCtrl', UserLocationCtrl);

    UserLocationCtrl.$inject = ['$scope', 'UserLocations', 'AlertNotification'];

    /**
     * @namespace UserLocationCtrl
     */
    function UserLocationCtrl($scope, UserLocations, AlertNotification) {
        var vm = this;
        
        
        // Declare functions
        vm.submit = submit;
        vm.edit = edit;
        vm.delete = destroy;
        vm.add = add;
        vm.cancelLocation = cancelLocation;

        //Declare vars
        vm.flag_update = false;
        vm.flag_create = false;

        vm.locations = [];
        vm.location = {};
        
        // TODO: provide a proper map center location
        $scope.map = {center: {latitude: -31.4179952, longitude: -64.1890513 }, zoom: 9 };
        $scope.options = {scrollwheel: false};

        vm.location_options = {
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
        };

        $scope.location_places = {};


        activate();

        function activate(){
            vm.promiseRequest = UserLocations.list().then(getLocationsSuccess, getLocationsError);

            function getLocationsSuccess(data){
                vm.locations = data.data;
                resetLocations();
            }

            function getLocationsError(data){
                AlertNotification.error("Error al intentar traer tus ubicaciones, vuelve a intentarlo");
            }
        }

        $scope.$watch('location_places', function(val, old_val){
           if($scope.location_places.geometry){
               vm.location.lat = angular.copy($scope.location_places.geometry.location.lat());
               vm.location.lng = angular.copy($scope.location_places.geometry.location.lng());
               //vm.location.title = angular.copy($scope.location_places.formatted_address);
               vm.location.center = {};
               vm.location.center.latitude = angular.copy($scope.location_places.geometry.location.lat());
               vm.location.center.longitude = angular.copy($scope.location_places.geometry.location.lng());
           }
        });

        function hideLocations() {
            for (var i=0; i < vm.locations.length; i++) {
                vm.locations[i].visible = false;
            }
        }

        function resetLocations() {
            // clean search places text box
            $('#google_places_ac').val('');
            // if a location wa being updated, set to original values
            if (vm.flag_update) {
                vm.location.center.latitude = vm.location.lat_original;
                vm.location.center.longitude = vm.location.lng_original;
                vm.location.radius = vm.location.radius_original;
            }
            vm.location = {};
            vm.flag_create = false;
            vm.flag_update = false;
            for (var i=0; i < vm.locations.length; i++) {
                vm.locations[i].visible = true;
                vm.locations[i].draggable = false;
                vm.locations[i].editable = false;
            }
        }

        function destroy(location) {
            vm.promiseRequest = UserLocations.destroy(location).then(deleteSuccess, deleteError);

            function deleteSuccess(data) {
                AlertNotification.success("La ubicacion '"+ location.title +"' se elimino con exito")
                vm.locations.splice(vm.locations.indexOf(location), 1);
            }
            function deleteError(data){
                AlertNotification.error("Error al intentar borrar la ubicacion seleccionada");
            }
            resetLocations();
        }

        function add(){
            vm.flag_create = true;
            hideLocations();
            vm.location = {radius: 10000, center: {}};
            vm.location.center.latitude = $scope.map.center.latitude;
            vm.location.center.longitude = $scope.map.center.longitude;
            vm.location.visible = true;
            vm.location.draggable = true;
            vm.location.editable = true;
        }

        function cancelLocation(){
            resetLocations();
        }

        function submit() {
            if(vm.flag_update){
                vm.location.lat = vm.location.center.latitude;
                vm.location.lng = vm.location.center.longitude;
                vm.promiseRequest = UserLocations.update(vm.location).then(submitSuccess, submitError);
            }else if(vm.flag_create){
                vm.promiseRequest = UserLocations.create(vm.location).then(submitSuccess, submitError);
            }

            function submitSuccess(data){
                if(vm.flag_update){
                    AlertNotification.success("La ubicacion seleccionada se edito con exito");
                    vm.flag_update = false;
                }else{
                    AlertNotification.success("Se ha agregado una ubicacion nueva");
                    vm.locations.push(data.data);
                    vm.location = {};
                }
                resetLocations();
            }

            function submitError(data){
                if(vm.flag_update){
                     AlertNotification.error("Error al intentar editar la ubicacion seleccionada");
                }else{
                    AlertNotification.error("Error al intentar agregar una nueva ubicacion");
                }
                resetLocations();
            }
        }

        /**
         * @Desc
         *
         */
        function edit(location){
            resetLocations();
            hideLocations();
            location.lat_original = location.lat;
            location.lng_original = location.lng;
            location.radius_original = location.radius;
            vm.location = location;
            $scope.map.center.latitude = vm.location.center.latitude;
            $scope.map.center.longitude = vm.location.center.longitude;
            location.draggable = true;
            location.editable = true;
            location.visible = true;
            vm.flag_update = true;
        }

    }
})();