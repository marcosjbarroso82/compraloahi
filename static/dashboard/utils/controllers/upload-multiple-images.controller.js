/**
 * UploadMultipleImagesController
 * @namespace dashBoardApp.util.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.util.controllers')
        .controller('UploadMultipleImagesController', UploadMultipleImagesController);

    UploadMultipleImagesController.$inject = ['$scope', 'fileReader'];

    /**
     * @namespace UploadMultipleImagesController
     */
    function UploadMultipleImagesController($scope, fileReader) {
        var vm = this;

        vm.imageDelete = imageDelete;
        vm.changeDefaultImage = changeDefaultImage;

        //vm.images = [];

        $scope.setFiles = function(element) {
            if (element.files[0] && 'name' in element.files[0]){
                var image = {is_new: true};
                fileReader.readAsDataUrl(element.files[0], $scope)
                    .then(function(result) {
                        image.image = result;
                        image.file = element.files[0];
                    });
                $scope.$apply(function(scope) {
                    scope.vm.images.push(image);
                });
            }
        };


        function imageDelete(image){
            if(image.is_new){
                vm.images.splice(vm.images.indexOf(image), 1);

            }else{
                image.deleted = true;
            }
        }

        function changeDefaultImage(image){
            for(var i=0; i < vm.images.length; i++){
                vm.images[i].default = false;
            }
            image.default = true;
        }
    }
})();