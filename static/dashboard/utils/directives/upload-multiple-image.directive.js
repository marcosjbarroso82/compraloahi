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
                uploadedImages: '@',
                itemId: '@'
            }
        };

        function link(scope, element, attrs) {
            scope.vm.itemId = attrs.itemId;
//            console.log("INIT DIREc");
//            console.log(scope.vm.itemId);

//            scope.$watch(attrs.itemId, function (value, new_val){
//                scope.vm.itemId = value;
//                console.log("CAMBIO");
//                console.log(value);
//                console.log(new_val);
//            });
//
//            attrs.$observe('itemId', function(value) {
//                console.log("CAMBIO1");
//                console.log(value);
//            });

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