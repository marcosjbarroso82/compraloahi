/**
 * UploadMultipleImagesController
 * @namespace dashBoardApp.util.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.util.controllers')
        .controller('UploadMultipleImagesController', UploadMultipleImagesController);

    UploadMultipleImagesController.$inject = ['$scope', 'fileReader', 'AlertNotification', 'ItemImages', 'ngDialog'];

    /**
     * @namespace UploadMultipleImagesController
     */
    function UploadMultipleImagesController($scope, fileReader, AlertNotification, ItemImages, ngDialog) {
        var vm = this;

        vm.imageDelete = imageDelete;
        vm.changeDefaultImage = changeDefaultImage;


        /////////////// -------------------------

        var getResizeArea = function () {
            var resizeAreaId = 'fileupload-resize-area';

            var resizeArea = document.getElementById(resizeAreaId);

            if (!resizeArea) {
                resizeArea = document.createElement('canvas');
                resizeArea.id = resizeAreaId;
                resizeArea.style.visibility = 'hidden';
                document.body.appendChild(resizeArea);
            }

            return resizeArea;
        };

        var resizeImage = function (origImage, options) {
            var maxHeight = 1024; //options.resizeMaxHeight || 300;
            var maxWidth = 1024; //options.resizeMaxWidth || 250;
            var quality = options.resizeQuality || 0.9;
            var type = options.resizeType || 'image/jpg';

            var canvas = getResizeArea();

            var height = origImage.naturalHeight;
            var width = origImage.naturalWidth;

            // calculate the width and height, constraining the proportions
            if (width > height) {
                if (width > maxWidth) {
                    height = Math.round(height *= maxWidth / width);
                    width = maxWidth;
                }
            } else {
                if (height > maxHeight) {
                    width = Math.round(width *= maxHeight / height);
                    height = maxHeight;
                }
            }
            canvas.width = width;
            canvas.height = height;

            //draw image on canvas
            var ctx = canvas.getContext("2d");
            ctx.drawImage(origImage, 0, 0, width, height);

            // get the data from canvas as 70% jpg (or specified type).
            return canvas.toDataURL(type, quality);
        };


        function uploadImage(image){
            // Upload image on server
            var element_img = angular.element('#img-' + angular.copy(image.key_prov))[0];
            image.resize_image = resizeImage(element_img, {'resizeType': image.type });

            if(vm.images.length == 1){
                image.default = true;
            }else{
                image.default = false;
            }

            image.ad = vm.itemId;
            ItemImages.create(image).then(successUpload, errorUpload);
//            if(image.id){
//                ItemImages.update(image).then(successUpload, errorUpload);
//            }else{
//                ItemImages.create(image).then(successUpload, errorUpload);
//            }

            function successUpload(data){
                AlertNotification.success("La imagen se cargo correctamente");
                    for(var i=0; i < vm.images.length; i++){
                        if(vm.images[i].name == image.name){
                            vm.images[i] = data.data;
                        }
                    }
            }

            function errorUpload(data){
                AlertNotification.error("Error al intentar cargar la imagen, vuelva a intentarlo");
                vm.images.splice(vm.images.indexOf(image), 1);
            }
        }

        ///////// -----------------------------------------
        $scope.setFiles = function(element) {
            if (element.files[0] && 'name' in element.files[0]){
                var image = {is_new: true};
                fileReader.readAsDataUrl(element.files[0], $scope)
                    .then(function(result) {
                        image.image = result;
                        image.name = element.files[0].name;
                        image.file = element.files[0];
                        image.type = element.files[0].type;
                        image.promise = true;
                        image.key_prov = String(image.$$hashKey).split(':')[1];

                        setTimeout(function(){
                            uploadImage(image);
                        }, 100);
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
            var message = '';

            if(vm.images.length > 1){
                if(image.default){
                    ngDialog.open({
                        className: 'ngdialog-theme-plain',
                        template: '<div class="dialog-contents">\
                                    <p><i class="fa fa-question-circle"> </i> Antes de eliminar una imagen destacada, por favor seleccione otra.</p>\
                                  </div>',
                        plain: true
                    });
                }else{
                    message = '¿Estas seguro que desea eliminar la imagen?';
                }
            }else{
                message = 'Al eliminar todas las imagenes de un aviso, este quedara inactivo \n ¿Estas seguro?';
            }

            if(message != ''){
                ngDialog.openConfirm({
                    className: 'ngdialog-theme-plain',
                    template: '<div class="dialog-contents">\
                                <p><i class="fa fa-question-circle"> </i> '+ message +'</p>\
                                <div class="ngdialog-buttons">\
                                    <button type="button" class="ngdialog-button ngdialog-button-secondary" ng-click="closeThisDialog(0)">CANCEL</button>\
                                    <button type="button" class="ngdialog-button ngdialog-button-primary" ng-click="confirm(1)">OK</button>\
                                </div> </div>',
                    plain: true
                }).then(function (data) {
                    if(data == 1){
                        ItemImages.destroy(image).then(successDelete, errorDelete);
                    }else{

                    }
                });
            }
            function successDelete(data){
                AlertNotification.success("La imagen se elimino exitosamente");
                vm.images.splice(vm.images.indexOf(image), 1);
            }

            function errorDelete(data){
                AlertNotification.error("Error al intentar eliminar la imagen. Vuelva a intentarlo.");
            }
        }

        function changeDefaultImage(image){

            ngDialog.openConfirm({
                    className: 'ngdialog-theme-plain',
                    template: '<div class="dialog-contents">\
                                <p><i class="fa fa-question-circle"> </i>A seleccionar una imagen como destacada, sera la imagen que tu aviso compite con otros avisos. ¿Estas seguro de cambiarla?</p>\
                                <div class="ngdialog-buttons">\
                                    <button type="button" class="ngdialog-button ngdialog-button-secondary" ng-click="closeThisDialog(0)">CANCEL</button>\
                                    <button type="button" class="ngdialog-button ngdialog-button-primary" ng-click="confirm(1)">OK</button>\
                                </div> </div>',
                    plain: true
                }).then(function (data) {
                    if(data == 1){
                        image.promise = true;
                        image.default = true;
                        ItemImages.change_default(image).then(successChangeDefault, errorChangeDefault);
                    }else{

                    }
                });

            function successChangeDefault(data){
                for(var i=0; i < vm.images.length; i++){
                    if(vm.images[i].id != image.id && vm.images[i].default){
                        vm.images[i].default = false;
                    }
                }
                image.promise = false;
                AlertNotification.success("Se ha cambiado la imagen destacada con exito.");
            }

            function errorChangeDefault(data){
                image.default = false;
                image.promise = false;
                AlertNotification.error("Error al intentar cambiar la imagen destacada. Vuelva a intentarlo mas tarde");
            }
        }
    }
})();