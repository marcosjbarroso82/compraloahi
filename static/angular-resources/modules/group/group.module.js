(function () {
    'use strict';

    angular
        .module('appGroup.group', [
            'appGroup.group.controllers',
            'appGroup.group.services'
        ]);

    angular
        .module('appGroup.group.controllers', ['ngDialog']);

    angular
        .module('appGroup.group.services', []);
})();