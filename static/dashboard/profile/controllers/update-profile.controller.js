/**
 * ProfileUpdateController
 * @namespace dashBoardApp.profile.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.profile.controllers')
        .controller('ProfileUpdateController', ProfileUpdateController);

    ProfileUpdateController.$inject = ['Profile', '$state', 'Snackbar', '$scope'];

    /**
     * @namespace ProfileUpdateController
     */
    function ProfileUpdateController(Profile, $state, Snackbar, $scope) {
        var vm = this;

        vm.profile = undefined;
        vm.submit = submit;
        vm.open = open;

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

        function open($event) {
          $event.preventDefault();
          $event.stopPropagation();

          vm.opened = true;
        };

        function submit(){
            vm.profile.img = $scope.img_profile;
            Profile.update(vm.profile).then(updateSuccess, updateError);

            function updateSuccess(data){
                Snackbar.show(data.data.message);
                $state.go('profile-detail');
            }

            function updateError(data){
                Snackbar.error("Error al intentar cambiar los datos");
            }
        }
    }


})();
