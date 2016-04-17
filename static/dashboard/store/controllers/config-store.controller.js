/**
 * StoreConfigCtrl
 * @namespace dashBoardApp.store.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.store.controllers')
        .controller('StoreConfigCtrl', StoreConfigCtrl);

    StoreConfigCtrl.$inject = ['Store', 'AlertNotification', '$scope', 'Item'];

    /**
     * @namespace ShopConfigCtrl
     */
    function StoreConfigCtrl(Store, AlertNotification, $scope, Item) {
        var vm = this;

        vm.submit = submit;
        vm.changeStoreName = changeStoreName;
        vm.nextStep = nextStep;
        vm.validateItemsSelect = validateItemsSelect;

        vm.configs = {};
        vm.configs.items = [];
        vm.logo = {};

        vm.name_unique = false;
        vm.name_is_valid = false;

        activate();

        function activate(){
            vm.promiseRequest = Store.getConfig().then(successConfig, errorConfig);

            function successConfig(data){
                vm.configs = data.data;

                changeStoreName();

                $scope.$watch('vm.configs.name', function(newValue, oldValue){
                    if(String(vm.configs.name).length > 3){
                        changeStoreName();
                        Store.is_name_valid(vm.configs.new_slug).then(isNameValidSuccess);
                    }

                    function isNameValidSuccess(data){
                        if (data.data.is_valid != 'true'){
                            vm.name_unique = true;
                            vm.name_is_valid = false;
                        }else{
                            vm.name_unique = false;
                            vm.name_is_valid = true;
                        }
                    }
                });
            }

            function errorConfig(data){
                AlertNotification.error("Se produjo un error en el servidor.");
            }

            vm.promiseRequestItems = Item.list().then(getItemSuccess, getItemError);

            function getItemSuccess(data){
                vm.configs.items = data.data;
            }

            function getItemError(data){
                console.log("Error request items");
            }
        }

        function validateItemsSelect(){
            if(vm.configs.items){
                for(var i=0; i < vm.configs.items.length; i++){
                    if(vm.configs.items[i].store_published){
                        return true;
                    }
                }
            }
            return false;
        }


        function submit(){
            vm.promiseRequest = Store.setConfig(vm.configs).then(submitSuccess, submitError);

            function submitSuccess(data){
                // TODO: make url with data response slug
                var slug = data.data.slug;
                AlertNotification.success("La tienda se configuro con exito. Ahora puedes ver tu tienda haciendo click <a href='/tienda/"+ slug +"' target='_blanck'>AQUI</a>");
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
            vm.configs.new_slug = String(angular.copy(vm.configs.name)).replace(/\s+/g,'-').toLowerCase();
        }

        function nextStep(){
            vm.step ++;
            if(vm.maxStep < vm.step){
                vm.maxStep = angular.copy(vm.step);
            }

        }



    }
})();
