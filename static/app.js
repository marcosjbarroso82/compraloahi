var App = angular.module('App', [
        // Third lib
        'ui.router',
        'ngResource',
        'ngSanitize',
        'uiGmapgoogle-maps',
        'ui.bootstrap',
        'cgBusy',
        // My lib
        'App.ad',
        'App.util'

    ])
    .config(function ($interpolateProvider, $httpProvider, $resourceProvider, $stateProvider) {

        // Force angular to use square brackets for template tag
        // The alternative is using {% verbatim %}
        $interpolateProvider.startSymbol('{{').endSymbol('}}');

        // CSRF Support
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

        // This only works in angular 3!
        // It makes dealing with Django slashes at the end of everything easier.
        $resourceProvider.defaults.stripTrailingSlashes = false;

        // Django expects jQuery like headers
        // $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';


    });
