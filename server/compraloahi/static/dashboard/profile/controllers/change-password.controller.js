/**
 * ChangePasswordController
 * @namespace dashBoardApp.profile.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.profile.controllers')
        .controller('ChangePasswordController', ChangePasswordController);

    ChangePasswordController.$inject = ['Profile', 'AlertNotification'];

    /**
     * @namespace ProfileUpdateController
     */
    function ChangePasswordController(Profile, AlertNotification) {
        var vm = this;

        vm.submit = submit;
        vm.password_is_valid = false;
        vm.passwordIsValid =passwordIsValid;

        function submit(){
            Profile.change_password(vm.user).then(updateSuccess, updateError);

            function updateSuccess(data){
                AlertNotification.success("La contraseña ha sido cambiada con exito");
                window.location.href = "/accounts/logout/";
            }

            function updateError(data){
                AlertNotification.error("Error al cambiar la contraseña");
            }
        }

        function passwordIsValid(){
            // var dummy
            var valid = false;
            if(valid){
                vm.password_is_valid = valid;
            }else{
                vm.password_is_valid = valid;
            }
        }

    }


})();