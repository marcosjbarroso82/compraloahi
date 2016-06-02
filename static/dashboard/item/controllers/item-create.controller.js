/**
 * ItemCtrl
 * @namespace dashBoardApp.item.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.item.controllers')
        .controller('ItemCreateCtrl', ItemCreateCtrl);

    ItemCreateCtrl.$inject = ['Item', 'AlertNotification', '$state', 'Authentication', 'Group'];

    /**
     * @namespace ItemCreateCtrl
     */
    function ItemCreateCtrl(Item, AlertNotification, $state, Authentication, Group){
        var vm = this;

        // Declare functions
        vm.submit = submit;
        vm.nextStep = nextStep;
        vm.selectCategory = selectCategory;
        vm.finish = finish;

        // Define vars
        vm.item = {
            body: '',
            groups: []
        };
        vm.item.categories = [];

        vm.categories_selected = [];

        vm.groups = [];
        vm.is_public = true;

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

                vm.promiseRequestGroup = Group.list().then(getGroupsSuccess, getGroupsError)
            }else{
                $state.go('profile-address', {"redirect": 'item-create'});
            }

            function getGroupsSuccess(data){
                vm.groups = data.data.results;
            }

            function getGroupsError(data){
                AlertNotification.error("Error al generar el formulario, intente recargando la pagina nuevamente.");
            }

            function getCategoriesSuccess(data){
                vm.categories = data.data.results;
            }

            function getCategoriesError(data){
                AlertNotification.error("Error al generar el formulario, intente recargando la pagina nuevamente.");
            }
        }


        function submit(){
            vm.item.categories = [vm.category_selected,];

            vm.item.groups = [];
            if(!vm.is_public){
                for(var i=0; i < vm.groups.length;i++){
                    if(vm.groups[i].selected){
                        vm.item.groups.push(vm.groups[i].id);
                    }
                }
            }

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