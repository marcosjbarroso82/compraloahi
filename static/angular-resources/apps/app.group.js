(function () {
    'use strict';

    angular.module('appGroup', [
        'froala',
        'appGroup.group'

    ]).config(config)
        .value('froalaConfig', {
            toolbarInline: false,
            placeholderText: 'Deja tu comentario...',
            toolbarBottom: true,
            toolbarButtons : ['insertLink', 'insertImage', 'insertVideo']
            //toolbarButtons : ['fullscreen', 'bold', 'italic', 'underline', 'strikeThrough', 'subscript', 'superscript', 'fontFamily', 'fontSize', '|', 'color', 'emoticons', 'inlineStyle', 'paragraphStyle', '|', 'paragraphFormat', 'align', 'formatOL', 'formatUL', 'outdent', 'indent', 'quote', 'insertHR', '-', 'insertLink', 'insertImage', 'insertVideo', 'insertFile', 'insertTable', 'undo', 'redo', 'clearFormatting', 'selectAll', 'html']
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
