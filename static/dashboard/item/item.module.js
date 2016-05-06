(function () {
    'use strict';

    angular
        .module('dashBoardApp.item', [
            'dashBoardApp.item.controllers',
            'dashBoardApp.item.services'
        ]);

    angular
        .module('dashBoardApp.item.controllers', ['ngDialog']);

    angular
        .module('dashBoardApp.item.services', []);
})();