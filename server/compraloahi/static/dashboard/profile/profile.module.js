(function () {
    'use strict';

    angular
        .module('dashBoardApp.profile', [
            'dashBoardApp.profile.controllers',
            'dashBoardApp.profile.services'
        ]);


    angular
        .module('dashBoardApp.profile.controllers', ['ngDialog']);

    angular
        .module('dashBoardApp.profile.services', []);


})();