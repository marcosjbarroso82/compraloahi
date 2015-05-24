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

        vm.configs = {};
        vm.logo = {};

        activate();

        function activate(){
            vm.promiseRequest = Store.getConfig().then(successConfig, errorConfig);

            function successConfig(data){
                vm.configs = data.data;
            }

            function errorConfig(data){
                AlertNotification.error("Se produjo un error en el servidor.");
            }

            vm.promiseRequest = Ad.get(function(data) {
                vm.configs.ads = data.results;
            });
        }


        function submit(){
            Store.setConfig(vm.configs);
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
            console.log("EL LOGO CAMBIO");
            upload_img();
        });



    }



})();
