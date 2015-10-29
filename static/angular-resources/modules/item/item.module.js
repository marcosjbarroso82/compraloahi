(function () {
    'use strict';

    angular
        .module('App.item', [
            'leaflet-directive',
            'tooltip',
            'util',
            'App.item.controllers',
            'App.item.services'
        ]);

    angular
        .module('App.item.controllers', []);

    angular
        .module('App.item.services', []);
})();
