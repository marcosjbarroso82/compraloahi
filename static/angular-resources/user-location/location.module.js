(function () {
    'use strict';

    angular
        .module('App.userLocation', [
            'App.userLocation.controllers',
            'App.userLocation.services'
        ]);

    angular
        .module('App.userLocation.controllers', []);

    angular
        .module('App.userLocation.services', ['ngResource']);
})();