/**
 * GroupCtrl
 * @namespace dashBoardApp.group.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.group.controllers')
        .controller('GroupCtrl', GroupCtrl);

    GroupCtrl.$inject = ['$scope', 'Group', 'AlertNotification'];

    /**
     * @namespace GroupCtrl
     */
    function GroupCtrl($scope, Group, AlertNotification) {

        var vm = this;

        // Declare functions
        vm.destroy = destroy;

        // Declare vars
        vm.groups = [];

        vm.request = false;



        function loadGroups(page_nro){
            vm.promiseRequest = Group.list().then(getSuccess, getError);

            function getSuccess(data){
                vm.groups = data.data.results;
                vm.request = true;
            }

            function getError(error){
                AlertNotification.error("Error al consultar los grupos, vuelva a intentarlo mas tarde");

                vm.request = true;
            }
        }

        init();

        function init(){
            loadGroups();
        }

        function destroy(group) {
            Group.destroy(group.id).then(deleteSuccess, deleteError);

            function deleteSuccess(data, headers, status){
                AlertNotification.success("El grupo " + group.title + " fue eliminado con exito!");
                vm.groups.splice(vm.groups.indexOf(group),1);
            }

            function deleteError(data, headers, status){
                AlertNotification.error("Error al intentar borrar el aviso");
            }
        }
    }
})();
