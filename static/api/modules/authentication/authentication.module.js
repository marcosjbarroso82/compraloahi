(function () {
    'use strict';

    angular
        .module('dashboard.authentication', [
            'dashboard.authentication.services',
            'dashboard.authentication.controllers'
        ]);

    angular
        .module('dashboard.authentication.services', ['ngCookies']);

    angular
        .module('dashboard.authentication.controllers', []);


})();