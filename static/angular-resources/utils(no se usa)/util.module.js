(function () {
    'use strict';

    angular
        .module('App.util', [
            'App.util.directives',
            'App.util.services'
        ]);

    angular
        .module('App.util.directives', ['ui.bootstrap']);

    angular
        .module('App.util.services', []);
})();






