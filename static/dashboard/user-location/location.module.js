(function () {
    'use strict';

    angular
        .module('dashBoardApp.userLocation', [
            'dashBoardApp.userLocation.controllers',
            'dashBoardApp.userLocation.services'
        ]);

    angular
        .module('dashBoardApp.userLocation.controllers', []);

    angular
        .module('dashBoardApp.userLocation.services', ['ngResource']);
})();