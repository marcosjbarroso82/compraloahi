/**
 * ItemCtrl
 * @namespace dashBoardApp.item.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.item.controllers')
        .controller('ItemCreateCtrl', ItemCreateCtrl);

    ItemCreateCtrl.$inject = ['Item', 'AlertNotification', '$state', 'Authentication'];

    /**
     * @namespace ItemCreateCtrl
     */
    function ItemCreateCtrl(Item, AlertNotification, $state, Authentication){
        var vm = this;

        // Declare functions
        vm.submit = submit;
        vm.nextStep = nextStep;
        vm.selectCategory = selectCategory;
        vm.finish = finish;

        // Define vars
        vm.item = {};
        vm.item.categories = [];

        vm.categories_selected = [];

        activate();

        function selectCategory(category){
            if(category.selected){
                vm.categories_selected.push(category.id);

            }else{
                vm.categories_selected.splice(vm.categories_selected.indexOf(category.id), 1);
            }
        }

        function activate(){

            if(Authentication.has_address){
                vm.promiseRequestCategories = Item.getCategories().then(getCategoriesSuccess, getCategoriesError);
            }else{
                $state.go('profile-address', {"redirect": 'item-create'});
            }

            function getCategoriesSuccess(data){
                vm.categories = data.data;
            }

            function getCategoriesError(data){
                AlertNotification.error("Error al generar el formulario, intente recargando la pagina nuevamente.");
            }
        }


        function submit(){
            vm.item.categories = [vm.category_selected,];

            vm.promiseRequest = Item.create(vm.item).then(createSuccess, createError);

            function createSuccess(data){
                Authentication.has_items = true;
                vm.item = data.data;
                AlertNotification.info("El aviso se creo correctamente, solo falta un paso.");
                nextStep();
            }
            function createError(data){
                AlertNotification.error("Error al intentar crear el aviso.");
            }
        }

        function finish(){
            $state.go('my-items');
        }

        function nextStep(){
            vm.step ++;
            if(vm.maxStep < vm.step){
                vm.maxStep = angular.copy(vm.step);
            }
        }
    }
})();