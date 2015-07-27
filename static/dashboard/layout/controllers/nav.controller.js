/**
 * LayoutCtrl
 * @namespace dashBoardApp.layout.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.layout.controllers')
        .controller('NavCtrl', NavCtrl);

    NavCtrl.$inject = ['Authentication'];

    /**
     * @namespace NavCtrl
     */
    function NavCtrl(Authentication) {
        var vm = this;

        vm.logout = logout;

        vm.msg_unread = Authentication.msg_unread;
        vm.notification_unread = Authentication.notification_unread;
        vm.profile = Authentication.profile;

        function logout(){
            Authentication.unauthenticate();
            window.location = '/users/logout/';
        }
    }

})();
