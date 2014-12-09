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
        $routeProvider.when('/api/v1/my-profile', {
            controller: 'ProfileDetailController',
            controllerAs: 'vm',
            templateUrl: '/static/api/tpl/profile/detail.html'
        }).otherwise('/api/v1/');
    }
})();