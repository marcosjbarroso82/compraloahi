/**
 * ProfileDetailController
 * @namespace App.profile.controllers
 */
(function () {
    'use strict';

    angular
        .module('App.profile.controllers')
        .controller('ProfileDetailController', ProfileDetailController);

    ProfileDetailController.$inject = ['Profile'];

    /**
     * @namespace ProfileDetailController
     */
    function ProfileDetailController(Profile) {
        var vm = this;

        vm.profile = undefined;

        activate();

        /**
         * @name activate
         * @desc Get Profile detail data
         * @memberOf App.authentication.controllers.ProfileDetailController
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