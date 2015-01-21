(function () {
    'use strict';

    angular
        .module('App.message', [
            'App.message.controllers',
            'App.message.services'
        ]);

    angular
        .module('App.message.controllers', []);

    angular
        .module('App.message.services', ['ngResource']);
})();