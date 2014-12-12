/**
 * ChangePasswordController
 * @namespace dashBoardApp.profile.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.profile.controllers')
        .controller('ChangePasswordController', ChangePasswordController);

    ChangePasswordController.$inject = ['Profile', '$location'];

    /**
     * @namespace ProfileUpdateController
     */
    function ChangePasswordController(Profile, $location) {
        var vm = this;

        vm.submit = submit;


        function submit(){
            Profile.change_password(vm.user).then(updateSuccess, updateError);

            function updateSuccess(data){
                $location.url('/');
            }

            function updateError(data){
                console.log("Error al editar el perfil");
            }
        }
    }


})();