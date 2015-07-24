(function () {
    'use strict';

    angular
        .module('App.ad', [
            'leaflet-directive',
            'tooltip',
            'dashBoardApp.util',
            'App.ad.controllers',
            'App.ad.services'
        ]);

    angular
        .module('App.ad.controllers', []);

    angular
        .module('App.ad.services', []);
})();
