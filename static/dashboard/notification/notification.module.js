(function () {
    'use strict';

    angular
        .module('dashBoardApp.notification', [
            'dashBoardApp.notification.controllers',
            'dashBoardApp.notification.services'
        ]);

    angular
        .module('dashBoardApp.notification.controllers', ['ngDialog']);

    angular
        .module('dashBoardApp.notification.services', []);
})();
