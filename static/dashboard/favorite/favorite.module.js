(function () {
    'use strict';

    angular
        .module('dashBoardApp.favorite', [
            'dashBoardApp.favorite.controllers',
            'dashBoardApp.favorite.services'
        ]);

    angular
        .module('dashBoardApp.favorite.controllers', []);

    angular
        .module('dashBoardApp.favorite.services', ['ngResource', 'djangoRESTResources']);
})();