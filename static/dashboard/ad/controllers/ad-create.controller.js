/**
 * AdCtrl
 * @namespace dashBoardApp.ad.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.ad.controllers')
        .controller('AdCreateCtrl', AdCreateCtrl);

    AdCreateCtrl.$inject = ['$scope', 'Ad', 'AlertNotification', '$timeout', 'UserLocations'];

    /**
     * @namespace AdCreateCtrl
     */
    function AdCreateCtrl($scope, Ad, AlertNotification, $timeout, UserLocations) {


        var vm = this;

        // Declare functions
        vm.submit = submit;
        vm.nextStep = nextStep;
        vm.selectCategory = selectCategory;


        vm.maxStep = 1;
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


        vm.options = {scrollwheel: false};

        $scope.map = { zoom: 14 };


        $scope.location_places = {};

        vm.user_locations = [];

        vm.categories_selected = [];
        ////////// Functions

        init();


        function nextStep(){
            vm.step ++;
            if(vm.maxStep < vm.step){
                vm.maxStep = angular.copy(vm.step);
            }

        }

        function selectCategory(category){
            if(category.selected){
                vm.categories_selected.push(category.id);

            }else{
                vm.categories_selected.splice(vm.categories_selected.indexOf(category.id), 1);
            }
        }

        function setDefaultLocation(){
            vm.location.center.latitude = -13.30272;
            vm.location.center.longitude = -87.144107;

            $scope.map.center = vm.location.center;

        }

        function init(){
            vm.promiseRequestCategories = Ad.getAllCategories().then(getCategoriesSuccess, getCategoriesError);

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
                vm.location.center.latitude = position.coords.latitude;
                vm.location.center.longitude = position.coords.longitude;
                $scope.map.center = vm.location.center;
            }

            function getError(err) {
                setDefaultLocation();
            }


            UserLocations.query(userLocationSuccess, userLocationError);

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

            vm.promiseRequest = Ad.create(vm.ad, $scope.interface.getFiles($scope.interface.FILE_TYPES.VALID)).then(createSuccess, createError);

            function createSuccess(data){
                if(vm.save_location && vm.custom_location == 'custom'){
                    UserLocations.save(vm.ad.locations[0]);
                }
                AlertNotification.success("El aviso se creo correctamente para ver el detalle presione <a href='http://compraloahi.com.ar' target='_blank'>aqui</a>.");
            }
            function createError(data){
                AlertNotification.error("Error al intentar crear el aviso");
            }
        }

        $scope.$watch('location_places', function(val, old_val){
            if($scope.location_places.geometry){
                //vm.location.title = angular.copy($scope.location_places.formatted_address);
                vm.location.center = {};
                vm.location.center.latitude = angular.copy($scope.location_places.geometry.location.lat());
                vm.location.center.longitude = angular.copy($scope.location_places.geometry.location.lng());
            }
        });


        /**
         * @property interface
         * @type {Object}
         */
        $scope.interface = {};

        /**
         * @property uploadCount
         * @type {Number}
         */
        $scope.uploadCount = 0;

        /**
         * @property success
         * @type {Boolean}
         */
        $scope.success = false;

        /**
         * @property error
         * @type {Boolean}
         */
        $scope.error = false;

        // Listen for when the interface has been configured.
        $scope.$on('$dropletReady', function whenDropletReady() {

            $scope.interface.allowedExtensions(['png', 'jpg']);
            $scope.interface.setRequestUrl('upload.html');
            $scope.interface.defineHTTPSuccess([/2.{2}/]);
            $scope.interface.useArray(false);

        });

        // Listen for when the files have been successfully uploaded.
        $scope.$on('$dropletSuccess', function onDropletSuccess(event, response, files) {

            $scope.uploadCount = files.length;
            $scope.success     = true;
            $timeout(function timeout() {
                $scope.success = false;
            }, 5000);

        });

        // Listen for when the files have failed to upload.
        $scope.$on('$dropletError', function onDropletError(event, response) {

            $scope.error = true;

            $timeout(function timeout() {
                $scope.error = false;
            }, 5000);

        });

    }
})();