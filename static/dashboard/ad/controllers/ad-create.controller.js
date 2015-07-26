/**
 * AdCtrl
 * @namespace dashBoardApp.ad.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.ad.controllers')
        .controller('AdCreateCtrl', AdCreateCtrl);

    AdCreateCtrl.$inject = ['$scope', 'Ad', 'AlertNotification', 'UserLocations', '$state', 'Authentication', 'leafletEvents', 'ngDialog'];

    /**
     * @namespace AdCreateCtrl
     */
    function AdCreateCtrl($scope, Ad, AlertNotification, UserLocations, $state, Authentication, leafletEvents, ngDialog) {
        var vm = this;

        // Declare functions
        vm.submit = submit;
        vm.nextStep = nextStep;
        vm.selectCategory = selectCategory;
        vm.changeLocationSelected =changeLocationSelected;

        // Define vars
        vm.ad = {};
        vm.ad.categories = [];

        vm.location = {};

        vm.user_locations = [];
        vm.categories_selected = [];

        vm.channel_set_location = 'userlocations'; // Flag to defined where is channel to set locations

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

        $scope.location_places = {};


        activate();


        function setDefaultLocation(){
            createMarker(-13.30272, -87.144107);
            vm.location.lat = -13.30272;
            vm.location.lng = -87.144107;
        }

        function changeLocationSelected(){
            if(vm.location_selected){
                vm.location = angular.copy(vm.location_selected);
            }
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
                }
            }
        }, true);

        function selectCategory(category){
            if(category.selected){
                vm.categories_selected.push(category.id);

            }else{
                vm.categories_selected.splice(vm.categories_selected.indexOf(category.id), 1);
            }
        }

        function activate(){
            vm.promiseRequestCategories = Ad.getCategories().then(getCategoriesSuccess, getCategoriesError);

            function getCategoriesSuccess(data){
                vm.categories = data.data;
            }

            function getCategoriesError(data){
                AlertNotification.error("Error al generar el formulario, intente recargando la pagina nuevamente.");
            }

            UserLocations.list().then(userLocationSuccess, userLocationError);

            function userLocationSuccess(data){
                vm.user_locations = data.data;
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
            vm.ad.locations = [];

            vm.ad.locations.push({lat: vm.location.lat , lng: vm.location.lng, title: (vm.location.title && vm.location.title != '') ? vm.location.title : 'Sin titulo' } );

            // TODO: remove image file on json
            vm.ad.images = vm.images;

            vm.promiseRequest = Ad.create(vm.ad, vm.images).then(createSuccess, createError);

            function createSuccess(data){
                if(vm.save_location && vm.channel_set_location == 'custom'){
                    UserLocations.create(vm.ad.locations[0]);
                }
                Authentication.has_ads = true;
                AlertNotification.success("El aviso se creo correctamente para ver el detalle presione <a href='http://compraloahi.com.ar' target='_blank'>aqui</a>.");
                $state.go('my-ads');
            }
            function createError(data){
                AlertNotification.error("Error al intentar crear el aviso");
            }
        }

        var flag_geo = false;

        function nextStep(){
            vm.step ++;
            if(vm.maxStep < vm.step){
                vm.maxStep = angular.copy(vm.step);
            }

            if(vm.maxStep == 4 && !flag_geo){
                flag_geo = true;
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
                            navigator.geolocation.getCurrentPosition(getCoords, getError);
                        } else {
                            setInitLocation();
                        }
                    }else{
                        setInitLocation();
                    }
                }, function(data){
                    setInitLocation();
                });

            }

            function getCoords(position) {
                vm.channel_set_location = 'custom';
                var lat = position.coords.latitude;
                var lng = position.coords.longitude;
                createMarker(lat, lng);
            }

            function getError(err) {
                setInitLocation();
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
                vm.channel_set_location = 'custom';
                setDefaultLocation();
            }else{
                createMarker(vm.user_locations[0].lat, vm.user_locations[0].lng);
                vm.location_selected = vm.user_locations[0];
            }
        }
    }
})();