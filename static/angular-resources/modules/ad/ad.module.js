(function () {
    'use strict';

    angular
        .module('App.ad', [
            'ngSanitize',
            'uiGmapgoogle-maps',
            'dashBoardApp.util',
            'App.ad.controllers',
            'App.ad.services'
        ]);

    angular
        .module('App.ad.controllers', []);

    angular
        .module('App.ad.services', []);
})();
