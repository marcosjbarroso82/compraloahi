/**
 * LayoutCtrl
 * @namespace dashBoardApp.layout.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.layout.controllers')
        .controller('SidebarCtrl', SidebarCtrl);

    SidebarCtrl.$inject = ['Authentication'];

    /**
     * @namespace SidebarCtrl
     */
    function SidebarCtrl(Authentication) {
        var vm = this;

        vm.has_ads = Authentication.has_ads;

    }

})();
