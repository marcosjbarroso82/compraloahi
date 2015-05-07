(function () {
    'use strict';

    angular
        .module('dashBoardApp.ad', [
            'dashBoardApp.ad.controllers',
            'dashBoardApp.ad.services'
        ]);

    angular
        .module('dashBoardApp.ad.controllers', ['ngDialog']);

    angular
        .module('dashBoardApp.ad.services', ['ngResource', 'djangoRESTResources']);
})();