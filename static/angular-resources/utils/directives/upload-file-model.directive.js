/**
 * Upload
 * @namespace App.util.directives
 */
(function () {
    'use strict';

    angular
        .module('App.util.directives')
        .directive('fileModel', fileModel);

    fileModel.$inject = ['$parse']
    /**
     * @namespace Select countries
     */
    function fileModel($parse) {
        /**
         * @name directive
         * @desc The directive to be returned
         * @memberOf App.util.directives.fileModel
         */
        var directive = {
            restrict: 'A',
            link: link
        };


        function link(scope, element, attrs) {
            var model = $parse(attrs.fileModel);
            var modelSetter = model.assign;

            element.bind('change', function(){
                scope.$apply(function(){
                    modelSetter(scope, element[0].files[0]);
                });
            });
        }

        return directive;
    }
})();