(function () {
    'use strict';

    angular
        .module('appSearch.config')
        .config(config);

    config.$inject = ['$locationProvider', '$httpProvider'];

    /**
     * @name config
     * @desc Enable HTML5 routing
     */
    function config($locationProvider, $httpProvider) {
        // CSRF Support
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

        $locationProvider.html5Mode(true).hashPrefix('!');
    }
})();
