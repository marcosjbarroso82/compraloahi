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
            .state('profile-address', {
                url: '/profile-address?redirect',
                templateUrl: '/static/dashboard/profile/templates/update-address.html',
                controller: 'ProfileAddressUpdateController',
                controllerAs: 'vm',
                data:{
                    breadcumbs: [
                        { url: 'profile-detail', name:'Perfil'},
                        { url: 'profile-address', name:'My ubicacion'}
                    ],
                    title: "Editar ubicacion"
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

            .state('config-privacity', {
                url: '/configuracion-privacidad/',
                templateUrl: '/static/dashboard/profile/templates/config-privacity.html',
                controller: 'ConfigPrivacityController',
                controllerAs: 'vm',
                data:{
                    breadcumbs: [
                        { url: 'profile-detail', name:'Perfil'},
                        { url: 'change-password', name:'Configura tu privacidad'}
                    ],
                    title: "Configura tu privacidad"
                }
            })

            // MESSAGE
            .state('messages', {
                url: '/mensajes/:folder',
                defaultParams: {folder: 'inbox'},
                templateUrl: '/static/dashboard/message/templates/messages-app.html',
                controller: 'MessageCtrl',
                controllerAs: 'vm',
                data:{
                    breadcumbs: [{url: "messages({'folder': 'inbox'})", name:'Mensajes'}],
                    title: "Mensajes"
                }
            })
            .state('message-thread', {
                url: '/mensajes/hilo/:id',
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
            .state('my-items', {
                url: '/mis-avisos/',
                templateUrl: '/static/dashboard/item/templates/item-list.html',
                controller: 'ItemCtrl',
                controllerAs: 'vm',
                data:{
                    breadcumbs: [{url: 'my-items', name:'Mis avisos'}],
                    title: "Mis avisos"
                }
            })

            // ADS CREATE
            .state('item-create', {
                url: '/mis-aviso/crear/',
                templateUrl: '/static/dashboard/item/templates/create.html',
                controller: 'ItemCreateCtrl',
                controllerAs: 'vm',
                data:{
                    breadcumbs: [
                        { url: 'my-items', name:'Mis avisos'},
                        { url: 'item-create', name:'Crear avisos'}
                    ],
                    title: "Crea tu avisos en 3 pasos"
                }
            })

            .state('item-update', {
                url: '/mis-aviso/update/:id',
                templateUrl: '/static/dashboard/item/templates/update.html',
                controller: 'ItemUpdateCtrl',
                controllerAs: 'vm',
                data:{
                    breadcumbs: [
                        { url: 'my-items', name:'Mis avisos'},
                        { url: 'item-update', name:'Editando avisos'}
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
            })

            // GROUPS
            .state('my-groups', {
                url: '/mis-grupos/',
                templateUrl: '/static/dashboard/group/templates/my-group-list.html',
                controller: 'GroupCtrl',
                controllerAs: 'vm',
                data:{
                    breadcumbs: [{url: 'mis-grupos', name:'Mis Grupos'}],
                    title: "Mis Grupos"
                }
            })
            .state('group-create', {
                url: '/crear-grupo/',
                templateUrl: '/static/dashboard/group/templates/create.html',
                controller: 'GroupCreateCtrl',
                controllerAs: 'vm',
                data:{
                    breadcumbs: [{url: 'crear-grupo', name:'Crear Grupo'}],
                    title: "Crear Grupos"
                }
            })
            .state('group-update', {
                url: '/editar-grupo/:id',
                templateUrl: '/static/dashboard/group/templates/update.html',
                controller: 'GroupUpdateCtrl',
                controllerAs: 'vm',
                data:{
                    breadcumbs: [{url: 'editar-grupo', name:'Editar Grupo'}],
                    title: "Editar Grupo"
                }
            });

            $urlRouterProvider.otherwise('/usuario/perfil/');

    }
})();
