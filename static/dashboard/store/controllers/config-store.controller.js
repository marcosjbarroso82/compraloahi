/**
 * StoreConfigCtrl
 * @namespace dashBoardApp.store.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.store.controllers')
        .controller('StoreConfigCtrl', StoreConfigCtrl);

    StoreConfigCtrl.$inject = ['Store', 'AlertNotification', '$scope', 'Ad'];

    /**
     * @namespace ShopConfigCtrl
     */
    function StoreConfigCtrl(Store, AlertNotification, $scope, Ad) {
        var vm = this;

        vm.submit = submit;
        vm.changeStoreName = changeStoreName;
        vm.nextStep = nextStep;
        vm.validateAdsSelect = validateAdsSelect;

        vm.configs = {};
        vm.configs.ads = [];
        vm.configs.backgroud_color = "#f9f9f9";
        vm.configs.font_color = "#000000";
        vm.logo = {};

        activate();

        function activate(){
            vm.promiseRequest = Store.getConfig().then(successConfig, errorConfig);

            function successConfig(data){
                vm.configs = data.data;
                if(vm.configs.name == 'Name'){
                    vm.configs.name = '';
                }
                changeStoreName();
            }

            function errorConfig(data){
                AlertNotification.error("Se produjo un error en el servidor.");
            }

            vm.promiseRequest = Ad.getAll().then(getAdSuccess, getAdError);

            function getAdSuccess(data){
                vm.configs.ads = data.data.results;
            }

            function getAdError(data){
                console.log("Error request ads");
            }
        }

        function validateAdsSelect(){
            if(vm.configs.ads){
                for(var i=0; i < vm.configs.ads.length; i++){
                    if(vm.configs.ads[i].store_published){
                        return true;
                    }
                }
            }
            return false;
        }


        function submit(){
            Store.setConfig(vm.configs).then(submitSuccess, submitError);

            function submitSuccess(data){
                AlertNotification.success("La tienda se configuro con exito. Ahora puedes ver tu tienda haciendo click <a href='/tienda/"+ vm.configs.url +"'>AQUI</a>");
            }

            function submitError(data){
                AlertNotification.error("Error al intentar configurar la tienda. Vuelva a intentarlo mas tarde");
            }
        }

        function upload_img(){

            if (vm.logo && 'name' in vm.logo){
                 vm.promise_img = Store.uploadImg(vm.logo).then(ChangeImgSuccess, ChangeImgError);
            }

            function ChangeImgSuccess(data, status, headers, config){
                vm.configs.logo = data.data.image_url;
                vm.logo = {};
            }

            function ChangeImgError(data, status, headers, config){
                 AlertNotification.error(data.error);
            }
        }

        $scope.$watch('vm.logo', function(){
            upload_img();
        });

        function changeStoreName(){
            vm.configs.url = String(angular.copy(vm.configs.name)).replace(/\s+/g,'-');
        }

        function nextStep(){
            vm.step ++;
            if(vm.maxStep < vm.step){
                vm.maxStep = angular.copy(vm.step);
            }

        }

    }



})();
