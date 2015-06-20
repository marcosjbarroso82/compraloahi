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
        'dashBoardApp.store'
    ])
    .value('cgBusyDefaults',{
        message:'Procesando solicitud...',
        backdrop: false,
        templateUrl: '/static/templates-utils/spinner.html',
        delay: 100,
        minDuration: 500,
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
    .config(function ($interpolateProvider, $httpProvider, $resourceProvider, $stateProvider, $urlRouterProvider, $locationProvider) {
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

        // Routing

        $urlRouterProvider.otherwise('/');

        $stateProvider
            // PROFILE
            .state('profile-detail', {
                url: '/usuario/perfil/',
                templateUrl: '/static/dashboard/profile/templates/detail-profile.html',
                controller: 'ProfileDetailController',
                controllerAs: 'vm'
            })
            .state('profile-update', {
                url: '/profile-update',
                templateUrl: '/static/dashboard/profile/templates/update-profile.html',
                controller: 'ProfileUpdateController',
                controllerAs: 'vm'
            })
            .state('change-password', {
                url: '/usuario/cambiar-contrasena/',
                templateUrl: '/static/dashboard/profile/templates/change-password.html',
                controller: 'ChangePasswordController',
                controllerAs: 'vm'
            })

            // MESSAGE
            .state('messages', {
                url: 'mensajes/?:folder',
                templateUrl: '/static/dashboard/message/templates/messages-app.html',
                controller: 'MessageCtrl',
                controllerAs: 'vm'
            })
            .state('message-thread', {
                url: 'mensajes/hilo/:id',
                templateUrl: '/static/dashboard/message/templates/messages-thread.html',
                controller: 'MessageThreadCtrl',
                controllerAs: 'vm'
            })

            // ADS
            .state('my-ads', {
                url: '/mis-avisos/',
                templateUrl: '/static/dashboard/ad/templates/ad-list.html',
                controller: 'AdCtrl',
                controllerAs: 'vm'
            })

            // ADS CREATE
            .state('ad-create', {
                url: '/aviso/crear/',
                templateUrl: '/static/dashboard/ad/templates/create.html',
                controller: 'AdCreateCtrl',
                controllerAs: 'vm'
            })

            // LOCATIONS
            .state('my-locations', {
                url: '/mis-ubicaciones/',
                templateUrl: '/static/dashboard/user-location/templates/user-locations-list.html',
                controller: 'UserLocationCtrl',
                controllerAs: 'vm'
            })
            // FAVORITE
            .state('favorites', {
                url: '/mis-favoritos/',
                templateUrl: '/static/dashboard/favorite/templates/list.html',
                controller: 'FavoriteCtrl',
                controllerAs: 'vm'
            })

            .state('config-notification', {
                url: '/notificaciones/configuracion/',
                templateUrl: '/static/dashboard/notification/templates/config-notification.html',
                controller: 'ConfigNotificationCtrl',
                controllerAs: 'vm'
            })

            .state('config-store', {
                url: '/tienda/configuracion/',
                templateUrl: '/static/dashboard/store/templates/config-store.html',
                controller: 'StoreConfigCtrl',
                controllerAs: 'vm'
            });


            $urlRouterProvider.otherwise('/usuario/perfil/');
    });

