/**
 * ProfileDetailController
 * @namespace dashBoardApp.profile.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.profile.controllers')
        .controller('ProfileDetailController', ProfileDetailController);

    ProfileDetailController.$inject = ['Profile', '$state'];

    /**
     * @namespace ProfileDetailController
     */
    function ProfileDetailController(Profile, $state) {
        var vm = this;

        vm.profile = undefined;

        activate();

        /**
         * @name activate
         * @desc Get Profile detail data
         * @memberOf dashBoardApp.authentication.controllers.ProfileDetailController
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


    }


})();