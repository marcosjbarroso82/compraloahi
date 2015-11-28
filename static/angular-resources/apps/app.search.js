(function () {
    'use strict';

    angular.module('appSearch', [
            'appSearch.config',
            'leaflet-directive',
            'tooltip',
            'appSearch.util',
            'appSearch.item'
        ]);

    angular
        .module('appSearch.config', []);


    angular
        .module('appSearch')
        .run(function(){
        });

    angular.bootstrap(document, ['appSearch']);
})();
