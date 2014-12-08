(function () {
    'use strict';

    angular
        .module('dashboard.routes')
        .config(config);

    config.$inject = ['$routeProvider'];

    /**
     * @name config
     * @desc Define valid application routes
     */
    function config($routeProvider) {
        $routeProvider.when('/dashboard/profile', {
            controller: 'ProfileDetailController',
            controllerAs: 'vm',
            templateUrl: '/static/api/tpl/profile/detail.html'
        }).otherwise('/dashboard');
    }
})();