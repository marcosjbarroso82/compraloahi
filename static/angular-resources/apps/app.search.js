(function () {
    'use strict';

    angular.module('App', [
            'App.ad'
        ])
    .config(function ($interpolateProvider, $httpProvider, $locationProvider) {
        $interpolateProvider.startSymbol('{{').endSymbol('}}');

        // CSRF Support
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

        $locationProvider.html5Mode(true).hashPrefix('!');

    });

    angular
        .module('App')
        .run(function(){

        });

})();
