(function () {
    'use strict';

    angular
        .module('dashBoardApp.location', [
            'dashBoardApp.location.controllers',
            'dashBoardApp.location.services'
        ]);

    angular
        .module('dashBoardApp.location.controllers', []);

    angular
        .module('dashBoardApp.location.services', ['ngResource']);
})();