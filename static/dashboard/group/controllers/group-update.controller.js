/**
 * GroupUpdateCtrl
 * @namespace dashBoardApp.group.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.group.controllers')
        .controller('GroupUpdateCtrl', GroupUpdateCtrl);

    GroupUpdateCtrl.$inject = ['$state', 'Group', 'AlertNotification', '$stateParams']; //, 'leafletEvents'];

    /**
     * @namespace GroupUpdateCtrl
     */
    function GroupUpdateCtrl($state, Group, AlertNotification, $stateParams){ //, leafletEvents) {
        var vm = this;

        vm.search_category = {};
        // Declare functions
        vm.submit = submit;
        vm.selectCategory = selectCategory;

        // Define vars
        vm.group = {};
        vm.group.categories = [];
        vm.group.images = [];


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

        vm.categories_selected = [];

        vm.request = false;

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

            // Get detail group. TODO: Groupd cache on service.
            vm.promiseRequest = Group.detail($stateParams.id).then(getGroupDetailSuccess, getGroupDetailError);

            function getGroupDetailSuccess(data){
                vm.group = data.data;
                vm.request = true;
                // Get categories
                vm.promiseRequestCategories = Group.getCategories().then(getCategoriesSuccess, getCategoriesError);
            }

            function getGroupDetailError(data){
                AlertNotification.error("Error al intentar cargar el aviso, Intenta nuevamente");
            }


            function getCategoriesSuccess(data){
                vm.categories = data.data;
                vm.category_selected = angular.copy(vm.group.categories[0]);
            }

            function getCategoriesError(data){
                AlertNotification.error("Error al generar el formulario, intente recargando la pagina nuevamente.");
            }
        }

        function submit(){
            vm.group.categories = [vm.category_selected,];

            vm.promiseRequest = Group.update(vm.group).then(updateSuccess, updateError);

            function updateSuccess(data){
                AlertNotification.success("El aviso se modifico correctamente para ver el detalle presione <a href='http://compraloahi.com.ar/group/'"+ vm.group.slug +" target='_blank'>aqui</a>.");
                $state.go('my-groups');
            }
            function updateError(data){
                AlertNotification.error("Error al intentar crear el aviso");
            }
        }

    }
})();