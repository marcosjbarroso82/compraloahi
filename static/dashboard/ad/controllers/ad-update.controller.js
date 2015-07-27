/**
 * AdUpdateCtrl
 * @namespace dashBoardApp.ad.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.ad.controllers')
        .controller('AdUpdateCtrl', AdUpdateCtrl);

    AdUpdateCtrl.$inject = ['$scope', 'Ad', 'AlertNotification', 'UserLocations', '$stateParams', 'leafletEvents'];

    /**
     * @namespace AdUpdateCtrl
     */
    function AdUpdateCtrl($scope, Ad, AlertNotification, UserLocations, $stateParams, leafletEvents) {


        var vm = this;

        // Declare functions
        vm.submit = submit;
        vm.selectCategory = selectCategory;
        vm.changeLocationSelected = changeLocationSelected;
        vm.setGeoLocation = setGeoLocation;

        // Define vars
        vm.ad = {};
        vm.ad.categories = [];
        vm.ad.images = [];

        vm.location = {};
        vm.location.center = {};

        vm.editorOptions = {
            language: 'es',
            uiColor: '#FFFFFF',
            toolbar: [
                ["Format", "Bold", "Italic", "Underline", "Strike", "SpellChecker", 'TextColor'],
                ['NumberedList', 'BulletedList', "Indent", "Outdent", 'JustifyLeft', 'JustifyCenter',
                    'JustifyRight', 'JustifyBlock'],
                ["Table", "Link", "Unlink", "SectionLink", "Subscript", "Superscript"], ['Undo', 'Redo'],
                ["Maximize"]
            ]
        };

        vm.channel_set_location = 'userlocations'; // Flag to defined where is channel to set locations

        vm.map = {
            center: {
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

        vm.user_locations = [];

        vm.categories_selected = [];

        vm.request = false;

        $scope.location_places = {}; // Var to search places

        activate();


        /**
         * Function to select user locations.
         */
        function changeLocationSelected(){
            if(vm.location_selected){
                vm.location.lat = angular.copy(vm.location_selected.lat);
                vm.location.lng = angular.copy(vm.location_selected.lng);
            }
        }


        /**
         * When change set location, change center map, and marker.
         */
        $scope.$watch('vm.location', function(new_val, old_val){
            if(vm.location.lat && vm.location.lng){
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
            }
        }, true);

        /**
         * When select location places, set center on location.
         */
        $scope.$watch('location_places', function(val, old_val){
            if($scope.location_places.geometry){
                vm.location.lat = angular.copy($scope.location_places.geometry.location.lat());
                vm.location.lng = angular.copy($scope.location_places.geometry.location.lng());
            }
        }, true);


        function selectCategory(category){
            if(category.selected){
                vm.categories_selected.push(category.id);
            }else{
                vm.categories_selected.splice(vm.categories_selected.indexOf(category.id), 1);
            }
        }

        /**
         * Function execute when inizialice controller
         */
        function activate(){

            // Get detail ad. TODO: Add cache on service.
            vm.promiseRequest = Ad.detail($stateParams.id).then(getAdDetailSuccess, getAdDetailError);

            function getAdDetailSuccess(data){
                vm.ad = data.data;
                vm.request = true;
                createMarker(vm.ad.locations[0].lat, vm.ad.locations[0].lng);
                vm.channel_set_location = 'custom';
                vm.images = angular.copy(vm.ad.images);
                vm.location.lat = angular.copy(vm.ad.locations[0].lat);
                vm.location.lng = angular.copy(vm.ad.locations[0].lng);


                // Get categories
                vm.promiseRequestCategories = Ad.getCategories().then(getCategoriesSuccess, getCategoriesError);
            }

            function getAdDetailError(data){
                AlertNotification.error("Error al intentar cargar el aviso, Intenta nuevamente");
            }


            function getCategoriesSuccess(data){
                vm.categories = data.data;
                for(var i=0; i < vm.ad.categories.length; i++){
                    for(var c=0; c < vm.categories.length; c++){
                        if(vm.ad.categories[i] == vm.categories[c].id){
                            vm.categories[c].selected = true;
                            vm.categories_selected.push(vm.categories[c].id);
                            break;
                        }
                    }
                }
            }

            function getCategoriesError(data){
                AlertNotification.error("Error al generar el formulario, intente recargando la pagina nuevamente.");
            }



            // Get user locations.
            UserLocations.list().then(userLocationSuccess, userLocationError);

            function userLocationSuccess(data){
                vm.user_locations = data.data;
                if(vm.user_locations.length  == 0){
                    vm.channel_set_location = 'custom';
                }
            }

            function userLocationError(data){
                vm.channel_set_location = 'custom'; //Set true by havent user locations
            }
        }

        function submit(){
            for(var i=0; i < vm.categories.length; i++){
                if(vm.categories[i].selected){
                    vm.ad.categories.push(vm.categories[i].id);
                }
            }

            vm.ad.locations[0].lat = vm.location.lat;
            vm.ad.locations[0].lng = vm.location.lng;

            // TODO: remove image file on json
            vm.ad.images = vm.images;

            vm.promiseRequest = Ad.update(vm.ad, vm.images).then(updateSuccess, updateError);

            function updateSuccess(data){
                if(vm.save_location && vm.channel_set_location == 'custom'){
                    UserLocations.create(vm.ad.locations[0]);
                }
                AlertNotification.success("El aviso se modifico correctamente para ver el detalle presione <a href='http://compraloahi.com.ar' target='_blank'>aqui</a>.");
                $state.go('my-ads');
            }
            function updateError(data){
                AlertNotification.error("Error al intentar crear el aviso");
            }
        }

        function createMarker(lat, lng){
            var marker = {
                lat: lat,
                lng: lng,
                icon: {
                    iconUrl: '/static/image/compraloahi_marker.svg',
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
                    vm.map.center.lat = lat;
                    vm.map.center.lng = lng;
                });
            }else{
                vm.map.markers["location"] = marker;
                vm.map.center.lat = lat;
                vm.map.center.lng = lng;
            }
        }


        function setGeoLocation(){
            if(navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(getCoords, getError);
            }

            function getCoords(position) {
                vm.location.lat = angular.copy(position.coords.latitude);
                vm.location.lng = angular.copy(position.coords.longitude);
            }

            function getError(err) {
                AlertNotification.error("Error al intentar consultar su ubicacion gps");
            }
        }

    }
})();