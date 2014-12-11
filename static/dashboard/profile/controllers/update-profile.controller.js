/**
 * ProfileUpdateController
 * @namespace dashBoardApp.profile.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.profile.controllers')
        .controller('ProfileUpdateController', ProfileUpdateController);

    ProfileUpdateController.$inject = ['Profile', '$location'];

    /**
     * @namespace ProfileUpdateController
     */
    function ProfileUpdateController(Profile, $location) {
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
                console.log(data);
            }

        }


        function submit(){
            Profile.update(vm.profile).then(updateSuccess, updateError);

            function updateSuccess(data){
                $location.url('/');
            }

            function updateError(data){
                console.log("ERror al editar el perfil");
            }
        }
    }


})();