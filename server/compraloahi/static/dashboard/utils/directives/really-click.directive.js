/**
 *
 * @namespace dashBoardApp.util.directives
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.util.directives')
        .directive('ngReallyClick', ngReallyClick);

    ngReallyClick.$inject = ['ngDialog'];

    /**
     * @name ngReallyClick
     * @desc The directive to easy add message confirm
     */
    function ngReallyClick(ngDialog) {


        return {
            restrict: 'A',
            scope:{
                ngReallyClick:"&", //declare a function binding for directive
                item:"=" //the current item for the directive
            },
            link: function(scope, element, attrs, $scope) {
                element.bind('click', function() {
                    var message = attrs.ngReallyMessage || "Are you sure?";
                    // TODO: https://github.com/likeastore/ngDialog
                    var dialog = ngDialog.openConfirm({
                        className: 'ngdialog-theme-plain',
                        template: '<div class="dialog-contents">\
                            <p><i class="fa fa-question-circle"> </i>  ' + message + '</p>\
                            <div class="ngdialog-buttons">\
                                <button type="button" class="ngdialog-button ngdialog-button-secondary" ng-click="closeThisDialog(0)">CANCEL</button>\
                                <button type="button" class="ngdialog-button ngdialog-button-primary" ng-click="confirm(1)">OK</button>\
                            </div> </div>',
                        plain: true

                    });

                    dialog.then(function (data) {
                        if(data == 1){
                            scope.ngReallyClick({item:scope.item});
                        }
                    });
                });

            }
        };

    }
})();