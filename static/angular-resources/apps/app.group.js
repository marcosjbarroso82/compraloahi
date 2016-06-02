(function () {
    'use strict';

    angular.module('appGroup', [
            'appSearch.util',
            'froala',
            'appGroup.group'

        ]).config(config)
        .value('froalaConfig', {
            toolbarInline: false,
            placeholderText: 'Deja tu comentario...',
            toolbarBottom: true,
            toolbarButtons : ['insertLink', 'insertImage', 'insertVideo']
        });

    config.$inject = ['$locationProvider', '$httpProvider'];

    /**
     * @name config
     * @desc Enable HTML5 routing
     */
    function config($locationProvider, $httpProvider) {
        // CSRF Support
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        $locationProvider.html5Mode(true).hashPrefix('!');
    }


    angular
        .module('appGroup')
        .run(function(){
        });

    angular.bootstrap(document, ['appGroup']);
})();
