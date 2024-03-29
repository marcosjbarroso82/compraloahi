/**
 * GroupCtrl
 * @namespace dashBoardApp.group.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.group.controllers')
        .controller('GroupCreateCtrl', GroupCreateCtrl);

    GroupCreateCtrl.$inject = ['Group', 'AlertNotification', '$state'];

    /**
     * @namespace GroupCreateCtrl
     */
    function GroupCreateCtrl(Group, AlertNotification, $state){
        var vm = this;

        // Declare functions
        vm.submit = submit;
        vm.finish = finish;

        // Define vars
        vm.group = {
            name: '',
            short_description: '',
            description: ''
        };

        function submit(){
            if (vm.image && 'name' in vm.image){
                // TODO: Resize image before sending it
                vm.group.image = vm.image;
            }
            if (vm.image_header && 'name' in vm.image_header){
                // TODO: Resize image before sending it
                vm.group.image_header = vm.image_header;
            }
            vm.promiseRequest = Group.create(vm.group).then(createSuccess, createError);

            function createSuccess(data){
                vm.group = data.data;
                AlertNotification.info("El group se creo correctamente!");
                finish();
            }
            function createError(data){
                AlertNotification.error("Error al intentar crear el group.");
            }
        }

        function finish(){
            $state.go('my-groups');
        }
    }
})();