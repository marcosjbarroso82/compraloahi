/**
 * ProfileDetailController
 * @namespace dashboard.profile.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashboard.profile.controllers')
        .controller('ProfileDetailController', ProfileDetailController);

    ProfileDetailController.$inject = ['Authentication', 'Profile'];

    /**
     * @namespace ProfileDetailController
     */
    function ProfileDetailController(Authentication, Profile) {
        var vm = this;

        vm.profile = undefined;

        activate();

        /**
         * @name activate
         * @desc Get Profile detail data
         * @memberOf app.authentication.controllers.ProfileDetailController
         */
        function activate() {
            Profile.detail().then(detailSuccess, detailError);


            function detailSuccess(data){
                vm.profile = data.data;
                vm.user = Authentication.getAuthenticatedAccount()
            }

            function detailError(data){
                console.log(data);
            }

        }


    }


})();