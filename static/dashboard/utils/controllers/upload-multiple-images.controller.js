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

        $scope.setFiles = function(element) {
            if (element.files[0] && 'name' in element.files[0]){
                var image = {is_new: true};
                fileReader.readAsDataUrl(element.files[0], $scope)
                    .then(function(result) {
                        image.image = result;
                        image.name = element.files[0].name;
                        image.file = element.files[0];

                    });
                $scope.$apply(function(scope) {
                        if(scope.vm.images.length == 0){
                            image.default = true;
                        }
                    scope.vm.images.push(image);
                });
            }
        };


        function imageDelete(image){
            // If image delete is default change default by next image.
            if(image.default){
                if(vm.images.length > 1){
                    var index = vm.images.indexOf(image);
                    for(var i=0; i < vm.images.length; i++){
                        if(i != index){
                            if(!vm.images[i].deleted){
                                vm.images[i].default = true;
                                break;
                            }
                        }
                    }
                }
            }
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