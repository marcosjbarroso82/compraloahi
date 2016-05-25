(function () {
    'use strict';

    angular.module('dashBoardApp', [

            // Third lib
            'ui.router',
            'tooltip',
            'cgBusy',
            'angularValidator',
            'nsPopover',
            'ng-currency',
            'ngTable',
            'leaflet-directive',
            '720kb.socialshare',
            'froala',
            'dashBoardApp.config',
            'dashBoardApp.routes',

            // My lib
            'authentication',
            'dashBoardApp.layout',
            'dashBoardApp.profile',
            'dashBoardApp.item',
            'dashBoardApp.group',
            'dashBoardApp.message',
            'dashBoardApp.userLocation',
            'dashBoardApp.util',
            'dashBoardApp.favorite',
            'dashBoardApp.notification',
            'dashBoardApp.store'
        ])
        .value('cgBusyDefaults',{
            message:'Procesando solicitud...',
            backdrop: false,
            templateUrl: '/static/templates-utils/spinner.html',
            delay: 100,
            minDuration: 500,
            wrapperClass: 'cg-busy cg-busy-backdrop'
        })
        .value('froalaConfig', {
            toolbarInline: false,
            placeholderText: 'Deja tu comentario...',
            //toolbarButtons : ['insertLink', 'insertImage', 'insertVideo']
            toolbarButtons : ['fullscreen', 'bold', 'italic', 'underline', 'strikeThrough', 'subscript', 'superscript', 'fontFamily', 'fontSize', '|', 'color', 'emoticons', 'inlineStyle', 'paragraphStyle', '|', 'paragraphFormat', 'align', 'formatOL', 'formatUL', 'outdent', 'indent', 'quote', 'insertHR', '-', 'insertLink', 'insertTable', 'undo', 'redo', 'clearFormatting', 'selectAll']
        });

    angular
        .module('dashBoardApp.routes', ['ui.router']);

    angular
        .module('dashBoardApp.config', []);

    angular
        .module('dashBoardApp')
        .run(function(){

        });

})();