/**
 * GroupUpdateCtrl
 * @namespace appGroup.group.controllers
 */
(function () {
    'use strict';

    angular
        .module('appGroup.group.controllers')
        .controller('GroupUpdateCtrl', GroupUpdateCtrl);

    GroupUpdateCtrl.$inject = ['$state', 'Group', 'AlertNotification', '$stateParams'];

    /**
     * @namespace GroupUpdateCtrl
     */
    function GroupUpdateCtrl($state, Group, AlertNotification, $stateParams){ //, leafletEvents) {
        var vm = this;

        // Declare functions
        vm.submit = submit;
        vm.finish = finish;

        // Define vars
        vm.group = {};

        function activate(){

            // Get detail group.
            vm.promiseRequest = Group.detail($stateParams.id).then(getGroupDetailSuccess, getGroupDetailError);

            function getGroupDetailSuccess(data){
                vm.group = data.data;
                vm.request = true;
            }

            function getGroupDetailError(data){
                AlertNotification.error("Error al intentar cargar el grupo, Intenta nuevamente");
            }
        }

        function submit(){
            if (vm.image && 'name' in vm.image){
                // TODO: Resize image before sending it
                vm.group.image = vm.image;
            }
            vm.promiseRequest = Group.update(vm.group).then(updateSuccess, updateError);

            function updateSuccess(data){
                console.log("updateSuccess" + data);
                vm.group = data.data;
                AlertNotification.info("El group se actualizo correctamente!");
                finish();
            }
            function updateError(data){
                console.log("updateError" + data);
                console.log(data);
                AlertNotification.error("Error al intentar actualizar el group.");
            }
        }

        function finish(){
                $state.go('my-groups');
        }
        activate();
    }
})();