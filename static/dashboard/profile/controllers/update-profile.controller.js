/**
 * ProfileUpdateController
 * @namespace dashBoardApp.profile.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.profile.controllers')
        .controller('ProfileUpdateController', ProfileUpdateController);

    ProfileUpdateController.$inject = ['Profile', '$state', 'Snackbar'];

    /**
     * @namespace ProfileUpdateController
     */
    function ProfileUpdateController(Profile, $state, Snackbar) {
        var vm = this;

        vm.profile = undefined;
        vm.submit = submit;

        activate();

        /**
         * @name activate
         * @desc Get Profile detail data
         * @memberOf dashBoardApp.authentication.controllers.ProfileUpdateController
         */
        function activate() {
            Profile.detail().then(detailSuccess, detailError);


            function detailSuccess(data){
                vm.profile = data.data;

            }

            function detailError(data){
                Snackbar.error("Error al cargar los datos de su perfil. Intente cargar de nuevo la pagina");
            }

        }


        function submit(){
            Profile.update(vm.profile).then(updateSuccess, updateError);

            function updateSuccess(data){
                Snackbar.show("Los datos se cambiaron con exito!");
                $state.go('profile-detail');
            }

            function updateError(data){
                Snackbar.error("Error al intentar cambiar los datos");
            }
        }
    }


})();