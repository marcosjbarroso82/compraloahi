(function () {
    'use strict';

    angular.module('appSearch', [
            'leaflet-directive',
            'tooltip',
            'appSearch.util',
            'appSearch.item'
        ]).config(config);

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


    angular
        .module('appSearch')
        .run(function(){
        });

    angular.bootstrap(document, ['appSearch']);
})();
