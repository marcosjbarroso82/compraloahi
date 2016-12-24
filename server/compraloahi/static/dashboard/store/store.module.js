(function () {
    'use strict';

    angular
        .module('dashBoardApp.store', [
            'dashBoardApp.store.controllers',
            'dashBoardApp.store.services'
        ]);

    angular
        .module('dashBoardApp.store.controllers', ['ngDialog']);

    angular
        .module('dashBoardApp.store.services', []);
})();