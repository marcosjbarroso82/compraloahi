/**
 * UserLocationCtrl
 * @namespace dashBoardApp.location.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.userLocation.controllers')
        .controller('UserLocationCtrl', UserLocationCtrl);

    UserLocationCtrl.$inject = ['$scope', 'UserLocations', 'AlertNotification', 'leafletEvents', 'leafletData', 'ngDialog'];

    /**
     * @namespace UserLocationCtrl
     */
    function UserLocationCtrl($scope, UserLocations, AlertNotification, leafletEvents, leafletData, ngDialog) {
        var vm = this;


        // Declare functions
        vm.submit = submit;
        vm.edit = edit;
        vm.delete = destroy;
        vm.add = add;
        vm.cancelLocation = cancelLocation;
        vm.selectLocation = selectLocation;
        vm.isSelected = isSelected;

        //Declare vars
        vm.flag_update = false;
        vm.flag_create = false;

        vm.locations = [];
        vm.location = {};


        vm.map = {
            center: {
                //autoDiscover: true, // Request locations by browser
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


        $scope.location_places = {};

        var select_location = select_location;


        activate();

        function activate(){

            vm.promiseRequest = UserLocations.list().then(getLocationsSuccess, getLocationsError);

            function getLocationsSuccess(data){
                vm.locations = data.data;
                initMap();
            }

            function getLocationsError(data){
                AlertNotification.error("Error al intentar traer tus ubicaciones, vuelve a intentarlo");
            }
        }

        function initMap(){
            leafletData.getMap("location-map").then(function(map) {
                vm.map.instance = map;


                vm.geo_location = {};
                if(map._initialCenter){
                    vm.geo_location['lat'] = angular.copy(map._initialCenter.lat);
                    vm.geo_location['lng'] = angular.copy(map._initialCenter.lng);
                }else{
                    // TODO: Quitar ubicacion por defecto en caso que no tenga acceso a la ubicacion del navegador y
                    // en caso de seleccionar geoLocation volver a preguntar pedir permisos al navegador si aun no lo tiene.
                    vm.search_location.geo_location['lat'] = -31.4179952;
                    vm.search_location.geo_location['lat'] = -64.1890513;
                }
                if(vm.locations.length > 0){
                    createMapLocation(vm.locations[0]['lat'], vm.locations[0]['lng'], vm.locations[0]['radius']);
                    vm.location = angular.copy(vm.locations[0]);
                }
            });
        }

        function createMapLocation(lat, lng, radius){
            var marker = {
                lat: lat,
                lng: lng,
                icon: {
                    iconUrl: '/static/image/custom_position_marker.svg',
                    shadowUrl: '/static/image/custom_position_marker_shadow.png',
                    iconSize: [25, 25],  // size of the icon
                    iconAnchor:   [12, 12], // point of the icon which will correspond to marker's location
                    popupAnchor: [0, -10], // point from whtich the popup should open relative to the iconAnchor
                    shadowAnchor: [10, -6], // the same for the shadow
                    shadowSize: [25, 10] // size of the shadow
                }
            };
            vm.map.markers["loc_selected"] = marker;
            vm.map.center.lat = angular.copy(lat);
            vm.map.center.lng = angular.copy(lng);

            vm.map.radius = L.circle([lat, lng], angular.copy(radius)).addTo(vm.map.instance);
        }



        function selectLocation(loc){
            if(!vm.flag_create && !vm.flag_update){
                select_location = angular.copy(loc);

                vm.location = angular.copy(loc);
                vm.map.markers['loc_selected']['lat'] = angular.copy(loc['lat']);
                vm.map.markers['loc_selected']['lng'] = angular.copy(loc['lng']);

                vm.map.center.lat = angular.copy(loc.lat);
                vm.map.center.lng = angular.copy(loc.lng);

                vm.map.radius.setRadius(angular.copy(loc['radius']));
                vm.map.radius.setLatLng([angular.copy(loc['lat']), angular.copy(loc['lng'])]);
            }
        }


        function isSelected(loc){
            if(!vm.flag_create || vm.flag_update){
                if(vm.location.id == loc.id){
                    return true
                }
            }
            return false;
        }

        $scope.$watch('location_places', function(val, old_val){
            if($scope.location_places.geometry){
                vm.location.lat = angular.copy($scope.location_places.geometry.location.lat());
                vm.location.lng = angular.copy($scope.location_places.geometry.location.lng());

                vm.map.markers['loc_selected']['lat'] = angular.copy(vm.location.lat);
                vm.map.markers['loc_selected']['lng'] = angular.copy(vm.location.lng);

                vm.map.center.lat = angular.copy(vm.location.lat);
                vm.map.center.lng = angular.copy(vm.location.lng);

                vm.map.radius.setLatLng([angular.copy(vm.location.lat), angular.copy(vm.location.lng)]);
            }
        });


        function resetLocations() {
            if(select_location && select_location['id']){
                selectLocation(select_location);
            }else{
                selectLocation(vm.locations[0])
            }
            vm.flag_create = false;
            vm.flag_update = false;
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

        $scope.$watch('vm.location.radius',function(val,old){
            if(val != old){
                vm.location.radius = parseInt(val);

                vm.map.radius.setRadius(vm.location.radius);
            }
        });

        function add(){
            vm.flag_create = true;

            ngDialog.openConfirm({
                className: 'ngdialog-theme-plain',
                template: '<div class="dialog-contents">\
                            <p><i class="fa fa-question-circle"> </i> ¿Desea utilizar su ubicacion?</p>\
                            <div class="ngdialog-buttons">\
                                <button type="button" class="ngdialog-button ngdialog-button-secondary" ng-click="closeThisDialog(0)">CANCEL</button>\
                                <button type="button" class="ngdialog-button ngdialog-button-primary" ng-click="confirm(1)">OK</button>\
                            </div> </div>',
                plain: true
            }).then(function (data) {
                if(data == 1){
                    vm.map.center.autoDiscover=true;
                    var watchChangeCenter = $scope.$watch('vm.map.center.lat', function(old_val, new_val){
                        if(vm.map.center.lat != 0){
                            var loc = {lat: vm.map.center.lat, lng: vm.map.center.lng, radius: 6000};

                            vm.location = angular.copy(loc);
                            vm.map.markers['loc_selected']['lat'] = angular.copy(loc['lat']);
                            vm.map.markers['loc_selected']['lng'] = angular.copy(loc['lng']);

                            vm.map.center.lat = angular.copy(loc.lat);
                            vm.map.center.lng = angular.copy(loc.lng);

                            vm.map.radius.setLatLng([angular.copy(loc['lat']), angular.copy(loc['lng'])]);

                            watchChangeCenter();
                        }
                    });
                }else{

                }
            });

            vm.location.lat = angular.copy(vm.geo_location.lat);
            vm.location.lng = angular.copy(vm.geo_location.lng);
            vm.location.radius = 6000;

            vm.selected_loc = angular.copy(vm.geo_location);
            vm.map.markers['loc_selected']['lat'] = angular.copy(vm.geo_location['lat']);
            vm.map.markers['loc_selected']['lng'] = angular.copy(vm.geo_location['lng']);

            vm.map.center.lat = angular.copy(vm.geo_location.lat);
            vm.map.center.lng = angular.copy(vm.geo_location.lng);

            vm.map.radius.setRadius(angular.copy(6000));
            vm.map.radius.setLatLng([angular.copy(vm.geo_location['lat']), angular.copy(vm.geo_location['lng'])]);
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
                    for(var i=0; i < vm.locations.length; i++){
                        if(vm.locations[i].id == data.data.id){
                            vm.locations[i] = data.data;
                        }
                    }
                }else{
                    AlertNotification.success("Se ha agregado una ubicacion nueva");
                    vm.locations.push(data.data);
                    vm.location = {};
                    vm.flag_create = false;
                    selectLocation(data.data);

                }
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
        function edit(loc){
            vm.flag_update = true;
            selectLocation(loc);
        }

    }
})();