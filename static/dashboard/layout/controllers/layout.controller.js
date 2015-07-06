/**
 * LayoutCtrl
 * @namespace dashBoardApp.layout.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.layout.controllers')
        .controller('LayoutCtrl', LayoutCtrl);

    LayoutCtrl.$inject = ['$rootScope', '$scope'];

    /**
     * @namespace LayoutCtrl
     */
    function LayoutCtrl($rootScope, $scope) {
        var vm = this;

        $rootScope.$on('$stateChangeStart', function (event, toState, toParams) {
            vm.data = toState.data;
        });

    }

})();
