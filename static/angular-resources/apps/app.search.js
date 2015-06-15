var App = angular.module('App', [
        // Third lib
        'ui.router',
        'ngResource',
        'ngSanitize',
        'uiGmapgoogle-maps',
        // My lib
        'App.ad',
        'dashBoardApp.util'

    ]).value('cgBusyDefaults',{
              message:'Procesando solicitud...',
              backdrop: false,
              templateUrl: '/static/templates-utils/spinner.html',
              delay: 300,
              minDuration: 1000,
              wrapperClass: 'cg-busy cg-busy-backdrop'
        })
    .config(function ($interpolateProvider, $httpProvider, $resourceProvider, $locationProvider) {

        // Force angular to use square brackets for template tag
        // The alternative is using {% verbatim %}
        $interpolateProvider.startSymbol('{{').endSymbol('}}');

        // CSRF Support
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

        // This only works in angular 3!
        // It makes dealing with Django slashes at the end of everything easier.
        $resourceProvider.defaults.stripTrailingSlashes = false;

        $locationProvider.html5Mode(true).hashPrefix('!');
        // Django expects jQuery like headers
        // $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';


    });
