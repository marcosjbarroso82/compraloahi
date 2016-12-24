/**
 * LayoutCtrl
 * @namespace dashBoardApp.layout.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.layout.controllers')
        .controller('NavCtrl', NavCtrl);

    NavCtrl.$inject = ['Authentication', '$scope'];

    /**
     * @namespace NavCtrl
     */
    function NavCtrl(Authentication, $scope) {
        var vm = this;

        vm.logout = logout;



        $scope.$watch( function () { return Authentication.msg_unread(); }, function (data) {
            vm.msg_unread = Authentication.msg_unread();
          }, true);

        vm.notification_unread = Authentication.notification_unread;
        vm.profile = Authentication.profile;

        function logout(){
            Authentication.unauthenticate();
            window.location = '/users/logout/';
        }
    }

})();
