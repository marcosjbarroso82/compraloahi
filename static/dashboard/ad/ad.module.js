(function () {
    'use strict';

    angular
        .module('dashBoardApp.ad', [
            'dashBoardApp.ad.controllers',
            'dashBoardApp.ad.services'
        ]);

    angular
        .module('dashBoardApp.ad.controllers', []);

    angular
        .module('dashBoardApp.ad.services', ['ngResource']);
})();