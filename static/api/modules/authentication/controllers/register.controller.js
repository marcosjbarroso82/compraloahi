/**
 * Register controller
 * @namespace app.authentication.controllers
 */
(function () {
    'use strict';

    angular
        .module('app.authentication.controllers')
        .controller('RegisterController', RegisterController);

    RegisterController.$inject = ['$location', '$scope', 'Authentication'];

    /**
     * @namespace RegisterController
     */
    function RegisterController($location, $scope, Authentication) {
        var vm = this;

        vm.register = register;

        /**
         * @name register
         * @desc Register a new Company
         * @memberOf app.authentication.controllers.RegisterController
         */
        function register() {
            Authentication.register(vm.email, vm.password, vm.company_name);
        }

        /**
         * @name activate
         * @desc Actions to be performed when this controller is instantiated
         * @memberOf app.authentication.controllers.RegisterController
         */
        function activate() {
            // If the vm is authenticated, they should not be here.
            if (Authentication.isAuthenticated()) {
                $location.url('/');
            }
        }
    }

    /**
     * @name activate
     * @desc Actions to be performed when this controller is instantiated
     * @memberOf app.authentication.controllers.RegisterController
     */
    function activate() {
        // If the vm is authenticated, they should not be here.
        if (Authentication.isAuthenticated()) {
            $location.url('/');
        }
    }
})();