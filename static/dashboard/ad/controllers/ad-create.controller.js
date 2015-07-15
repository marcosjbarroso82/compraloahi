/**
 * AdCtrl
 * @namespace dashBoardApp.ad.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.ad.controllers')
        .controller('AdCreateCtrl', AdCreateCtrl);

    AdCreateCtrl.$inject = ['$scope', 'Ad', 'AlertNotification', 'UserLocations', '$state', 'Authentication'];

    /**
     * @namespace AdCreateCtrl
     */
    function AdCreateCtrl($scope, Ad, AlertNotification, UserLocations, $state, Authentication) {
        var vm = this;

        // Declare functions
        vm.submit = submit;
        vm.nextStep = nextStep;
        vm.selectCategory = selectCategory;
        vm.changeLocationSelected = changeLocationSelected;

        // Define vars
        vm.ad = {};
        vm.ad.categories = [];

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
        vm.user_locations = [];
        vm.categories_selected = [];

        vm.channel_set_location = 'userlocations'; // Flag to defined where is channel to set locations

        $scope.map = {center: {latitude: -31.4179952, longitude: -64.1890513 }, zoom: 15 };
        $scope.options = {scrollwheel: false};

        $scope.location_places = {};
        $scope.location = {center: {latitude: -31.4179952, longitude: -64.1890513 }};




        activate();

        function changeLocationSelected(){
            vm.location.center = angular.copy(vm.location_selected.center);

        }


        function setDefaultLocation(){
            console.log("set default location");
            vm.location.center = {};
            vm.location.center.latitude = -13.30272;
            vm.location.center.longitude = -87.144107;
        }

        $scope.$watch('vm.location.center', function(location, old_location){
            console.log("CAMBIO LOCATION");
            if(vm.location.center.latitude && vm.location.center.longitude){
                console.log(vm.location);
                $scope.map.center = angular.copy(vm.location.center);
                $scope.location.center = angular.copy(vm.location.center);

                console.log("MAP LOCATION");
                console.log(vm.location);
            }
        });

        $scope.$watch('location_places', function(val, old_val){
            if($scope.location_places.geometry){
                vm.location.center = {};
                vm.location.center.latitude = angular.copy($scope.location_places.geometry.location.lat());
                vm.location.center.longitude = angular.copy($scope.location_places.geometry.location.lng());
            }
        });



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

            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(getCoords, getError);
            } else {
                setDefaultLocation();
            }

            function getCoords(position) {
                vm.location.center = {};
                vm.location.center.latitude = angular.copy(position.coords.latitude);
                vm.location.center.longitude = angular.copy(position.coords.longitude);


            }

            function getError(err) {
                setDefaultLocation();
            }


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

            vm.ad.locations = [];
            if(vm.channel_set_location == 'custom'){
                vm.ad.locations.push(vm.location);
            }else{
                vm.ad.locations.push(vm.location_selected);
            }

            vm.ad.locations[0].lat = vm.ad.locations[0].center.latitude;
            vm.ad.locations[0].lng = vm.ad.locations[0].center.longitude;

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


        function nextStep(){
            vm.step ++;
            if(vm.maxStep < vm.step){
                vm.maxStep = angular.copy(vm.step);
            }
        }
    }
})();