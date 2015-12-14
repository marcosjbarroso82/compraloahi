/**
 * ProfileAddressUpdateController
 * @namespace dashBoardApp.profile.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.profile.controllers')
        .controller('ProfileAddressUpdateController', ProfileAddressUpdateController);

    ProfileAddressUpdateController.$inject = ['Profile', '$scope', 'AlertNotification', '$state', 'leafletEvents', 'ngDialog', '$stateParams', 'Authentication'];

    /**
     * @namespace ProfileAddressUpdateController
     */
    function ProfileAddressUpdateController(Profile, $scope, AlertNotification, $state, leafletEvents, ngDialog, $stateParams, Authentication) {
        var vm = this;

        vm.submit = submit;

        vm.user_locations = [];

        //vm.changeLocationSelected =changeLocationSelected;

        vm.location = {};

        vm.location.address = {};

        vm.map = {
            center: {
                lat: -31.4179952, lng: -64.1890513,
                autoDiscover: true, // Request locations by browser
                zoom: 14
            },
            events: {
                markers: {
                    enable: leafletEvents.getAvailableMarkerEvents()
                }
            },
            bounds: {},
            defaults: {
                maxZoom: 15,
                minZoom: 12,
                tileLayer: "http://otile2.mqcdn.com/tiles/1.0.0/osm/{z}/{x}/{y}.png",
                zoomControl: false
            },
            markers: {}
        };

        vm.redirect = 'profile-detail';

        $scope.location_places = {};

        vm.autorozired_location = autorozired_location;


        activate();

        /**
         * @name init
         * @desc function inizialize
         * @memberOf dashBoardApp.profile.controllers.ProfileAddressUpdateController
         */
        function activate() {

            if($stateParams.redirect){
                vm.redirect = $stateParams.redirect;
            }
            vm.promiseRequest = Profile.get_address().then(getAddressSuccess, getAddressError);

            function getAddressSuccess(data){
                vm.location = data.data;
                if(vm.location.lat && vm.location.lng){
                    createMarker(vm.location.lat, vm.location.lng);
                }else{
                    autorozired_location();
                }

            }

            function getAddressError(data){
                AlertNotification.error('Error al intentar cargar tu ubicacion, vuelva a intentarlo recargando la pagina');
            }
        }

        /**
         * @name submit
         * @desc submit form to update profile
         * @memberOf dashBoardApp.profile.controllers.ProfileAddressUpdateController
         */
        function submit(){
            vm.promiseRequest = Profile.update_address(vm.location).then(updateSuccess, updateError);

            function updateSuccess(data){
                Authentication.has_address = true;
                AlertNotification.success("La ubicacion personal se ha actualizado correctamente.");
                $state.go(vm.redirect);
            }

            function updateError(data){
                AlertNotification.error("Error al modificar el perfil");

            }
        }

        function setDefaultLocation(){
            createMarker(-13.30272, -87.144107);
            vm.location.lat = -13.30272;
            vm.location.lng = -87.144107;
        }

        $scope.$watch('vm.location', function(new_val, old_val){
            if(vm.location){
                if(new_val.lat != old_val.lat){
                    if(vm.map.markers['location']){
                        vm.map.markers["location"]['lat'] = vm.location.lat;
                    }
                    vm.map.center['lat'] = vm.location.lat;
                }
                if(new_val.lng != old_val.lng){
                    if(vm.map.markers['location']){
                        vm.map.markers["location"]['lng'] = vm.location.lng;
                    }
                    vm.map.center['lng'] = vm.location.lng;
                }
            }

        }, true);


        /**
         * When select location places, set center on location.
         */
        $scope.$watch('$$childTail.location_places', function(val, old_val){
            if ($scope.$$childTail && $scope.$$childTail['location_places']){
                if($scope.$$childTail.location_places.geometry){
                    vm.location.lat = angular.copy($scope.$$childTail.location_places.geometry.location.lat());
                    vm.location.lng = angular.copy($scope.$$childTail.location_places.geometry.location.lng());

                    vm.map.center.lat = vm.location.lat;
                    vm.map.center.lng = vm.location.lng;
                }
            }
        }, true);

        function autorozired_location(){
            ngDialog.openConfirm({
                className: 'ngdialog-theme-plain',
                template: '<div class="dialog-contents">\
                                    <p><i class="fa fa-question-circle"> </i> ¿Desea utilizar su ubicacion para crear este aviso?</p>\
                                    <div class="ngdialog-buttons">\
                                        <button type="button" class="ngdialog-button ngdialog-button-secondary" ng-click="closeThisDialog(0)">CANCEL</button>\
                                        <button type="button" class="ngdialog-button ngdialog-button-primary" ng-click="confirm(1)">OK</button>\
                                    </div> </div>',
                plain: true
            }).then(function (data) {
                if(data == 1){
                    if (navigator.geolocation) {
                        vm.promiseRequestLocation = navigator.geolocation.getCurrentPosition(getCoords, getError);
                    } else {
                        setInitLocation();
                    }
                }else{
                    setInitLocation();
                }
            }, function(data){
                setInitLocation();
            });

            function getCoords(position) {
                var lat = position.coords.latitude;
                var lng = position.coords.longitude;
                createMarker(lat, lng);
            }

            function getError(err) {
                AlertNotification.error("Error al intentar consultar su ubicacion, intenta agregando la direccion desde la caja de texto que aparece sobre el mapa");
                setInitLocation();
            }
        }


        function createMarker(lat, lng){
            var marker = {
                lat: lat,
                lng: lng,
                icon: {
                    iconUrl: '/static/image/map52.svg',
                    shadowUrl: '/static/image/markers-shadow.png',
                    iconSize: [35, 45],  // size of the icon
                    iconAnchor:   [17, 42], // point of the icon which will correspond to marker's location
                    popupAnchor: [1, -32], // point from which the popup should open relative to the iconAnchor
                    shadowAnchor: [10, 12], // the same for the shadow
                    shadowSize: [36, 16] // size of the shadow
                }
            };
            if(vm.channel_set_location == 'custom'){
                $scope.$apply(function(){
                    vm.map.markers["location"] = marker;
                    vm.location.lat = lat;
                    vm.location.lng = lng;
                });
            }else{
                vm.map.markers["location"] = marker;
                vm.location.lat = lat;
                vm.location.lng = lng;
            }

        }

        function setInitLocation(){
            if(vm.user_locations.length  == 0){
                setDefaultLocation();
            }else{
                //createMarker(vm.user_locations[0].lat, vm.user_locations[0].lng);
                //vm.location_selected = vm.user_locations[0];
            }
        }
    }

})();
