angular.module('dashBoardApp', [
        // Third lib
        'angular.snackbar',
        'ui.router',
        '720kb.tooltips',
        'ngResource',
        'cgBusy',
        'angularValidator',
        'nsPopover',
        'ng-currency',
        //'ngSanitize',
        'uiGmapgoogle-maps',
        'ngTable',
        // My lib
        'dashBoardApp.profile',
        'dashBoardApp.ad',
        'dashBoardApp.message',
        'dashBoardApp.userLocation',
        'dashBoardApp.util',
        'dashBoardApp.favorite',
        'dashBoardApp.notification',
        'dashBoardApp.store',
        'validation.match'

    ]).value('cgBusyDefaults',{
              message:'Procesando solicitud...',
              backdrop: false,
              templateUrl: '/static/templates-utils/spinner.html',
              delay: 300,
              minDuration: 1000,
              wrapperClass: 'cg-busy cg-busy-backdrop'
        })
    .run(function($rootScope, Message){
        $rootScope.new_messages_count = 0;
        Message.getUnreadCount().
            success(function(data, status, headers, config) {
                $rootScope.new_messages_count = data.count;
            }).
            error(function(data, status, headers, config) {
                $rootScope.new_messages_count = 0;
            });
    })
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
                templateUrl: '/static/dashboard/profile/templates/detail-profile.html',
                controller: 'ProfileDetailController',
                controllerAs: 'vm'
            })

            // PROFILE
            .state('profile-detail', {
                url: '/profile-detail',
                templateUrl: '/static/dashboard/profile/templates/detail-profile.html',
                controller: 'ProfileDetailController',
                controllerAs: 'vm'
            })
            //.state('profile-create', {
            //    url: '/profile-create',
            //    templateUrl: '/static/dashboard/profile/templates/create-profile.html',
            //    controller: 'ProfileCreateController',
            //    controllerAs: 'vm'
            //})
            .state('change-password', {
                url: '/profile/change-password',
                templateUrl: '/static/dashboard/profile/templates/change-password.html',
                controller: 'ChangePasswordController',
                controllerAs: 'vm'
            })

            // MESSAGE
            .state('messages', {
                url: 'messages/?:folder',
                templateUrl: '/static/dashboard/message/templates/messages-app.html',
                controller: 'MessageCtrl',
                controllerAs: 'vm'
            })
            .state('message-thread', {
                url: 'message-thread/:id',
                templateUrl: '/static/dashboard/message/templates/messages-thread.html',
                controller: 'MessageThreadCtrl',
                controllerAs: 'vm'
            })

            // ADS
            .state('my-ads', {
                url: '/my-ads',
                templateUrl: '/static/dashboard/ad/templates/ad-list.html',
                controller: 'AdCtrl',
                controllerAs: 'vm'
            })

            // ADS CREATE
            .state('ad-create', {
                url: '/ad-create',
                templateUrl: '/static/dashboard/ad/templates/create.html',
                controller: 'AdCreateCtrl',
                controllerAs: 'vm'
            })

            // LOCATIONS
            .state('my-locations', {
                url: '/my-locations',
                templateUrl: '/static/dashboard/user-location/templates/user-locations-list.html',
                controller: 'UserLocationCtrl',
                controllerAs: 'vm'
            })
            // FAVORITE
            .state('favorite', {
                url: '/my-favorites',
                templateUrl: '/static/dashboard/favorite/templates/list.html',
                controller: 'FavoriteCtrl',
                controllerAs: 'vm'
            })

            // AGENDA
            .state('agenda', {
                url: '/agenda',
                templateUrl: '/static/dashboard/agenda/templates/agenda.html'
            })

            .state('config-notification', {
                url: '/config-notification',
                templateUrl: '/static/dashboard/notification/templates/config-notification.html',
                controller: 'ConfigNotificationCtrl',
                controllerAs: 'vm'
            })

            .state('config-store', {
                url: '/config-store',
                templateUrl: '/static/dashboard/store/templates/config-store.html',
                controller: 'StoreConfigCtrl',
                controllerAs: 'vm'
            })
    });

