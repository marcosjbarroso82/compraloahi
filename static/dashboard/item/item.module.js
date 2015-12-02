(function () {
    'use strict';

    angular
        .module('dashBoardApp.item', [
            'dashBoardApp.item.controllers',
            'dashBoardApp.item.services',
            'ngCkeditor'
        ]);

    angular
        .module('dashBoardApp.item.controllers', ['ngDialog']);

    angular
        .module('dashBoardApp.item.services', []);
})();