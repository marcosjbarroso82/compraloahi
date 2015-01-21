var App = angular.module('App', [
        // Third lib
        'ui.router',
        'ngResource',
        'ngSanitize',
        'uiGmapgoogle-maps',
        'ui.bootstrap',

        // My lib
        'App.profile',
        'App.ad',
        'App.message',
        'App.userLocation',
        'App.util'

    ])
    .config(function ($interpolateProvider, $httpProvider, $resourceProvider, $stateProvider, $urlRouterProvider) {
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

        // Routing

        $urlRouterProvider.otherwise('/');

        $stateProvider
            .state('default', {
                url: '/',
                views: {
                    'ad-list': {
                        templateUrl: '/static/angular-resources/ad/templates/ad-list.html',
                        controller: 'AdCtrl'
                    },
                    'ad-map': {
                        templateUrl: '/static/angular-resources/ad/templates/ad.html',
                        controller: 'AdCtrl'
                    }
                }
            })
            // ADS
            .state('my-ads', {
                url: '/my-ads',
                templateUrl: '/static/angular-resources/ad/templates/ad-list.html',
                controller: 'AdCtrl'
            })

            // LOCATIONS
            .state('my-locations', {
                url: '/my-locations',
                templateUrl: '/static/angular-resources/user-location/templates/user-locations-list.html',
                controller: 'UserLocationCtrl'
            })
    })
;

