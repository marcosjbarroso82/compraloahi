(function () {
    'use strict';

    angular
        .module('dashBoardApp.routes')
        .config(config);

    config.$inject = ['$stateProvider', '$urlRouterProvider'];

    /**
     * @name config
     * @desc Define valid application routes
     */
    function config($stateProvider, $urlRouterProvider) {

        $stateProvider
            // PROFILE
            .state('profile-detail', {
                url: '/usuario/perfil/',
                templateUrl: '/static/dashboard/profile/templates/detail-profile.html',
                controller: 'ProfileDetailController',
                controllerAs: 'vm',
                data:{
                    breadcumbs: [{url: 'profile-detail', name:'Perfil'}],
                    title: "Mi perfil"
                }
            })
            .state('profile-update', {
                url: '/profile-update',
                templateUrl: '/static/dashboard/profile/templates/update-profile.html',
                controller: 'ProfileUpdateController',
                controllerAs: 'vm',
                data:{
                    breadcumbs: [
                        { url: 'profile-detail', name:'Perfil'},
                        { url: 'profile-update', name:'Editar'}
                    ],
                    title: "Editar perfil"
                }
            })
            .state('change-password', {
                url: '/usuario/cambiar-contrasena/',
                templateUrl: '/static/dashboard/profile/templates/change-password.html',
                controller: 'ChangePasswordController',
                controllerAs: 'vm',
                data:{
                    breadcumbs: [
                        { url: 'profile-detail', name:'Perfil'},
                        { url: 'change-password', name:'Cambiar contraseña'}
                    ],
                    title: "Cambiar contraseña"
                }
            })

            // MESSAGE
            .state('messages', {
                url: 'mensajes/?:folder',
                templateUrl: '/static/dashboard/message/templates/messages-app.html',
                controller: 'MessageCtrl',
                controllerAs: 'vm',
                data:{
                    breadcumbs: [{url: "messages({'folder': 'inbox'})", name:'Mensajes'}],
                    title: "Mensajes"
                }
            })
            .state('message-thread', {
                url: 'mensajes/hilo/:id',
                templateUrl: '/static/dashboard/message/templates/messages-thread.html',
                controller: 'MessageThreadCtrl',
                controllerAs: 'vm',
                data:{
                    breadcumbs: [
                        {url: "messages({'folder': 'inbox'})", name:'Mensajes'},
                        { url: 'message-thread', name:'Conversacion'}
                    ],
                    title: "Conversacion"
                }
            })

            // ADS
            .state('my-ads', {
                url: '/mis-avisos/',
                templateUrl: '/static/dashboard/ad/templates/ad-list.html',
                controller: 'AdCtrl',
                controllerAs: 'vm',
                data:{
                    breadcumbs: [{url: 'my-ads', name:'Mis avisos'}],
                    title: "Mis avisos"
                }
            })

            // ADS CREATE
            .state('ad-create', {
                url: '/mis-aviso/crear/',
                templateUrl: '/static/dashboard/ad/templates/create.html',
                controller: 'AdCreateCtrl',
                controllerAs: 'vm',
                data:{
                    breadcumbs: [
                        { url: 'my-ads', name:'Mis avisos'},
                        { url: 'ad-create', name:'Crear avisos'}
                    ],
                    title: "Crea tu avisos en 4 pasos"
                }
            })

            .state('ad-update', {
                url: '/mis-aviso/update/:id',
                templateUrl: '/static/dashboard/ad/templates/update.html',
                controller: 'AdUpdateCtrl',
                controllerAs: 'vm',
                data:{
                    breadcumbs: [
                        { url: 'my-ads', name:'Mis avisos'},
                        { url: 'ad-update', name:'Editando avisos'}
                    ],
                    title: "Editando aviso"
                }
            })

            // LOCATIONS
            .state('my-locations', {
                url: '/mis-ubicaciones/',
                templateUrl: '/static/dashboard/user-location/templates/user-locations-list.html',
                controller: 'UserLocationCtrl',
                controllerAs: 'vm',
                data:{
                    breadcumbs: [{url: 'my-locations', name:'Mis ubicaciones'}],
                    title: "Mis ubicaciones"
                }
            })
            // FAVORITE
            .state('favorites', {
                url: '/mis-favoritos/',
                templateUrl: '/static/dashboard/favorite/templates/list.html',
                controller: 'FavoriteCtrl',
                controllerAs: 'vm',
                data:{
                    breadcumbs: [{url: 'favorites', name:'Mis favoritos'}],
                    title: "Mis favoritos"
                }
            })

            .state('config-notification', {
                url: '/notificaciones/configuracion/',
                templateUrl: '/static/dashboard/notification/templates/config-notification.html',
                controller: 'ConfigNotificationCtrl',
                controllerAs: 'vm',
                data:{
                    breadcumbs: [
                        { url: 'profile-detail', name:'Perfil'},
                        {url: 'config-notification', name:'Configurar Alertas'}
                    ],
                    title: "Configurar Alertas"
                }
            })

            .state('config-store', {
                url: '/tienda/configuracion/',
                templateUrl: '/static/dashboard/store/templates/config-store.html',
                controller: 'StoreConfigCtrl',
                controllerAs: 'vm',
                data:{
                    breadcumbs: [
                        { url: 'profile-detail', name:'Perfil'},
                        {url: 'config-store', name:'Personalizar mi tienda'}
                    ],
                    title: "Personalizar mi tienda"
                }
            });

            $urlRouterProvider.otherwise('/usuario/perfil/');

    }
})();
