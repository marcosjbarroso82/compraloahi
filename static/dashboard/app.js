angular.module('dashBoardApp', [
        'ui.router',
        'ngResource',
        'dashBoardApp.services',
        'dashBoardApp.controllers',
        'dashBoardApp.profile',
        'dashBoardApp.ad',
        'dashBoardApp.message',
        'dashBoardApp.userLocation',
        'ngSanitize',
        'uiGmapgoogle-maps',
        'OtdDirectives'
    ])
    .config(function ($interpolateProvider, $httpProvider, $resourceProvider, $stateProvider, $urlRouterProvider) {
        // Force angular to use square brackets for template tag
        // The alternative is using {% verbatim %}
        $interpolateProvider.startSymbol('[[').endSymbol(']]');

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
            .state('my-ads', {
                url: '/my-ads',
                templateUrl: '/static/dashboard/ad/templates/ad-list.html',
                controller: 'AdCtrl'
            })
            .state('my-locations', {
                url: '/my-locations',
                templateUrl: '/static/dashboard/user-location/templates/user-locations-list.html',
                controller: 'UserLocationCtrl'
            })
            .state('profile-detail', {
                url: '/profile-detail',
                templateUrl: '/static/dashboard/profile/templates/detail-profile.html',
                controller: 'ProfileDetailController',
                controllerAs: 'vm'
            })
            .state('default', {
                url: '/',
                templateUrl: '/static/dashboard/profile/templates/detail-profile.html',
                controller: 'ProfileDetailController',
                controllerAs: 'vm'
            })
            .state('messages', {
                url: 'messages',
                templateUrl: '/static/dashboard/message/templates/messages-app.html',
                controller: 'MessageCtrl'
            })
            .state('message-thread', {
                url: 'message-thread/:id',
                templateUrl: '/static/dashboard/message/templates/messages-thread.html',
                controller: 'MessageThreadCtrl'
            })
			.state('profile-update', {
                url: '/profile-update',
                templateUrl: '/static/dashboard/profile/templates/update-profile.html',
                controller: 'ProfileUpdateController',
                controllerAs: 'vm'
            })
            .state('change-password', {
                url: '/profile/change-password',
                templateUrl: '/static/dashboard/profile/templates/change-password.html',
                controller: 'ChangePasswordController',
                controllerAs: 'vm'
            })
    });
