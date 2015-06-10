/**
 * ChangePasswordController
 * @namespace dashBoardApp.profile.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.profile.controllers')
        .controller('ChangePasswordController', ChangePasswordController);

    ChangePasswordController.$inject = ['Profile', '$state', 'AlertNotification'];

    /**
     * @namespace ProfileUpdateController
     */
    function ChangePasswordController(Profile, $state, AlertNotification) {
        var vm = this;

        vm.submit = submit;


        function submit(){
            Profile.change_password(vm.user).then(updateSuccess, updateError);

            function updateSuccess(data){
                $state.go('profile-detail');
                //AlertNotification.success("La contraseña ha sido cambiada con exito");
                window.location.href = "/accounts/login/";
            }

            function updateError(data){
                AlertNotification.error("Error al cambiar la contraseña");
            }
        }
    }


})();