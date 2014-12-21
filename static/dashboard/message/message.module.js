(function () {
    'use strict';

    angular
        .module('dashBoardApp.message', [
            'dashBoardApp.message.controllers',
            'dashBoardApp.message.services'
        ]);

    angular
        .module('dashBoardApp.message.controllers', []);

    angular
        .module('dashBoardApp.message.services', ['ngResource']);
})();