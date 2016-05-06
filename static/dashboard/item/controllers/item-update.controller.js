/**
 * ItemUpdateCtrl
 * @namespace dashBoardApp.item.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.item.controllers')
        .controller('ItemUpdateCtrl', ItemUpdateCtrl);

    ItemUpdateCtrl.$inject = ['$state', 'Item', 'AlertNotification', '$stateParams', 'Group']; //, 'leafletEvents'];

    /**
     * @namespace ItemUpdateCtrl
     */
    function ItemUpdateCtrl($state, Item, AlertNotification, $stateParams, Group){ //, leafletEvents) {
        var vm = this;

        vm.search_category = {};
        // Declare functions
        vm.submit = submit;
        vm.selectCategory = selectCategory;

        // Define vars
        vm.item = {
            body: '',
            groups: []
        };
        vm.item.categories = [];
        vm.item.images = [];

        vm.categories_selected = [];

        vm.request = false;

        vm.is_public = false;

        activate();

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

            // Get detail item. TODO: Itemd cache on service.
            vm.promiseRequest = Item.detail($stateParams.id).then(getItemDetailSuccess, getItemDetailError);

            function getItemDetailSuccess(data){
                vm.item = data.data;
                vm.request = true;
                // Get categories
                vm.promiseRequestCategories = Item.getCategories().then(getCategoriesSuccess, getCategoriesError);
                vm.promiseRequestGroup = Group.list().then(getGroupsSuccess, getGroupsError)
            }

            function getGroupsSuccess(data){
                vm.groups = data.data.results;
                if(vm.item.groups.length > 0){
                    for(var i=0; i < vm.item.groups.length; i++){
                        angular.forEach(vm.groups, function(group) {
                           if(group.id == vm.item.groups[i]){
                               group.selected = true;
                               //break; # TODO: break doesnt work with angular.forEarch
                           }
                        });
                    }
                }else{
                    vm.is_public = true;
                }
            }

            function getGroupsError(data){
                AlertNotification.error("Error al generar el formulario, intente recargando la pagina nuevamente.");
            }

            function getItemDetailError(data){
                AlertNotification.error("Error al intentar cargar el aviso, Intenta nuevamente");
            }


            function getCategoriesSuccess(data){
                vm.categories = data.data.results;
                vm.category_selected = angular.copy(vm.item.categories[0]);
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
                        vm.item.groups.append(vm.groups[i].id);
                    }
                }
            }

            vm.promiseRequest = Item.update(vm.item).then(updateSuccess, updateError);

            function updateSuccess(data){
                AlertNotification.success("El aviso se modifico correctamente para ver el detalle presione <a href='http://compraloahi.com.ar/item/'"+ vm.item.slug +" target='_blank'>aqui</a>.");
                $state.go('my-items');
            }
            function updateError(data){
                AlertNotification.error("Error al intentar crear el aviso");
            }
        }

    }
})();