/**
 *
 * @namespace App.util.directives
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.util.directives')
        .directive('ngEnter', ngEnter);

    ngEnter.$inject = [];

    /**
     * Directive to watch key enter press . ex use:  ng-enter="myfunc()"
     * @returns {Function}
     */
    function ngEnter() {
        return function (scope, element, attrs) {
        element.bind("keydown keypress", function (event) {
            if(event.which === 13) {
                scope.$apply(function (){
                    scope.$eval(attrs.ngEnter);
                });

                event.preventDefault();
            }
        });
    };

    }
})();