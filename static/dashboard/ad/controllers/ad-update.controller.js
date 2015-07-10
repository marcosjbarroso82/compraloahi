/**
 * AdUpdateCtrl
 * @namespace dashBoardApp.ad.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.ad.controllers')
        .controller('AdUpdateCtrl', AdUpdateCtrl);

    AdUpdateCtrl.$inject = ['$scope', 'Ad', 'AlertNotification', '$timeout', 'UserLocations', '$stateParams', 'fileReader'];

    /**
     * @namespace AdUpdateCtrl
     */
    function AdUpdateCtrl($scope, Ad, AlertNotification, $timeout, UserLocations, $stateParams, fileReader) {


        var vm = this;

        // Declare functions
        vm.submit = submit;
        vm.selectCategory = selectCategory;
        vm.changeLocationSelected = changeLocationSelected;

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


        $scope.map = {zoom: 15 }; // Var to map
        $scope.options = {scrollwheel: false}; // Var to options map

        $scope.location_places = {}; // Var to search places

        $scope.location = {center: {}}; //Var to select places on map

        vm.user_locations = [];

        vm.categories_selected = [];

        vm.request = false;

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

        /**
         * Function execute when inizialice controller
         */
        function activate(){

            vm.promiseRequest = Ad.detail($stateParams.id).then(getAdDetailSuccess, getAdDetailError);

            function getAdDetailSuccess(data){
                vm.ad = data.data;
                vm.request = true;
                vm.location.center = vm.ad.locations[0].center;
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
                            break;
                        }
                    }
                }
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
                vm.user_locations = data;
            }

            function userLocationError(data){
                vm.custom_location = true; //Set true by havent user locations
            }
        }

        function submit(){

            for(var i=0; i < vm.categories.length; i++){
                if(vm.categories[i].selected){
                    vm.ad.categories.push(vm.categories[i].id);
                }
            }

            vm.ad.locations = [];
            if(vm.custom_location == 'custom'){
                vm.ad.locations.push(vm.location);
            }else{
                vm.ad.locations.push(vm.location_selected);
            }

            vm.ad.locations[0].lat = vm.ad.locations[0].center.latitude;
            vm.ad.locations[0].lng = vm.ad.locations[0].center.longitude;

            vm.promiseRequest = Ad.create(vm.ad).then(createSuccess, createError);

            function createSuccess(data){
                if(vm.save_location && vm.custom_location == 'custom'){
                    UserLocations.save(vm.ad.locations[0]);
                }
                AlertNotification.success("El aviso se creo correctamente para ver el detalle presione <a href='http://compraloahi.com.ar' target='_blank'>aqui</a>.");
                $state.go('my-ads');
            }
            function createError(data){
                AlertNotification.error("Error al intentar crear el aviso");
            }
        }


    }
})();