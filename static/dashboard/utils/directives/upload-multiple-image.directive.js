/**
 * Upload
 * @namespace dashBoardApp.util.directives
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.util.directives')
        .directive('uploadImages', uploadImages);

    uploadImages.$inject = ['$parse']
    /**
     * @namespace uploadImages
     */
    function uploadImages($parse) {

        var directive = {
            controller: 'UploadMultipleImagesController as vm',
            restrict: 'EA',
            templateUrl: '/static/dashboard/utils/templates/upload-multiple-images.html',
            link: link,
            scope: {
                filesModel: '@',
                uploadedImages: '@'
            }
        };

        function link(scope, element, attrs) {

            if(attrs.uploadedImages){
                scope.vm.images = eval(attrs.uploadedImages);
            }else{
                scope.vm.images = [];
            }
            element.bind('change', function(){
                scope.$apply(function(){
                    scope.$parent.vm[attrs.filesModel] = scope.vm.images;
                });
            });
        }

        return directive;
    }
})();