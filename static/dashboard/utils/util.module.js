(function () {
    'use strict';

    angular
        .module('dashBoardApp.util', [
            'dashBoardApp.util.directives',
            'dashBoardApp.util.services'
        ]);

    angular
        .module('dashBoardApp.util.directives', ['ui.bootstrap']);

    angular
        .module('dashBoardApp.util.services', []);
})();






