/**
 * MessageCtrl
 * @namespace dashBoardApp.message.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.message.controllers')
        .controller('MessageCtrl', MessageCtrl);

    MessageCtrl.$inject = ['$scope', 'Message', 'Snackbar'];

    /**
     * @namespace MessageCtrl
     */
    function MessageCtrl($scope, Message, Snackbar) {
        $scope.messages = {};
        $scope.message = {};

        $scope.loadMessages = function(folder){
            Message.getMsgs(folder).then(getSuccess, getError);
            $scope.folder = folder;
            function getSuccess(data){
                $scope.messages = data.data;

            };

            function getError(data){
                console.log('Error al cargar el inbox');
            }
        }

        $scope.delete_bulk = function(){
            var messages = [];
            for(var i=0; i < $scope.messages.length; i++){
                if($scope.messages[i].selected){
                    messages.push($scope.messages[i]);
                }
            }

            Message.delete_bulk(messages).then(deleteSuccess, deleteError);

            function deleteSuccess(data, headers, status){
                Snackbar.show("Los mensajes seleccionados se eliminaron con exito");
                console.log(data.data);
                $scope.loadMessages($scope.folder);
            }

            function deleteError(data, headers, status){
                Snackbar.error("Error al intentar eliminar mensajes seleccionados");
            }
        }

        $scope.messages = $scope.loadMessages('inbox');
    }


})();