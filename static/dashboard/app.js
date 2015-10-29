(function () {
    'use strict';

    angular.module('dashBoardApp', [

            // Third lib
            'angular.snackbar',
            'ui.router',
            'tooltip',
            'cgBusy',
            'angularValidator',
            'nsPopover',
            'ng-currency',
            'ngTable',
            'leaflet-directive',

            'dashBoardApp.config',
            'dashBoardApp.routes',

            // My lib
            'authentication',
            'dashBoardApp.layout',
            'dashBoardApp.profile',
            'dashBoardApp.item',
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
        });

    angular
        .module('dashBoardApp.routes', ['ui.router']);

    angular
        .module('dashBoardApp.config', []);

    angular
        .module('dashBoardApp')
        .run(function(){

        });

})();