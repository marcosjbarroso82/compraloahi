/**
 *
 * @namespace App.util.directives
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.util.directives')
        .directive('imageonload', ImageOnLoad);

    ImageOnLoad.$inject = [];


    function ImageOnLoad() {
        return {
            restrict: 'A',
            link: function(scope, element, attrs) {
                element.bind('load', function() {
                    console.log("loading....")
                });
            }
        };

    }
})();