/**
 * ChangePasswordController
 * @namespace App.profile.controllers
 */
(function () {
    'use strict';

    angular
        .module('App.profile.controllers')
        .controller('ChangePasswordController', ChangePasswordController);

    ChangePasswordController.$inject = ['Profile', '$state', 'Snackbar'];

    /**
     * @namespace ProfileUpdateController
     */
    function ChangePasswordController(Profile, $state, Snackbar) {
        var vm = this;

        vm.submit = submit;


        function submit(){
            Profile.change_password(vm.user).then(updateSuccess, updateError);

            function updateSuccess(data){
                $state.go('profile-detail');
                Snackbar.show("La contraseña ha sido cambiada con exito");
            }

            function updateError(data){
                Snackbar.show("Error al cambiar la contraseña");
            }
        }
    }


})();