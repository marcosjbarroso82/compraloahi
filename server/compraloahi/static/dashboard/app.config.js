(function () {
    'use strict';

    angular
        .module('dashBoardApp.config')
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

        // This only works in angular 3!
        // It makes dealing with Django slashes at the end of everything easier.
        //$resourceProvider.defaults.stripTrailingSlashes = false;

        $locationProvider.html5Mode(true).hashPrefix('!');

    }
})();
