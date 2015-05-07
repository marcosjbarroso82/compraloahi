/**
 * MessageCtrl
 * @namespace dashBoardApp.message.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.message.controllers')
        .controller('MessageCtrl', MessageCtrl);

    MessageCtrl.$inject = ['$scope', 'Message', 'AlertNotification', '$stateParams'];

    /**
     * @namespace MessageCtrl
     */
    function MessageCtrl($scope, Message, AlertNotification, $stateParams) {
        $scope.messages = {};
        $scope.message = {};
        $scope.messages_selected = [];
        $scope.page = 1;
        $scope.count = 0;

        $scope.loadMessages = function(folder){
            Message.getMsgs(folder, 0).then(getMessagesByFolderSuccess, getMessagesByFolderError);
            $scope.folder = folder;
            
        }

        $scope.select_all_messages = function(){
            angular.forEach($scope.messages, function(message){
               message.selected = $scope.messages_select;
            });

            if($scope.messages_select){
                $scope.messages_selected = $scope.messages;
            }else{
                $scope.messages_selected = [];
            }
        }
        
        $scope.select_message = function(message){
            // If message has state selected add to array messages_selected, else, remove.
            if(message.selected){
                $scope.messages_selected.push(message);
            }else{
                $scope.messages_selected.splice($scope.messages_selected.indexOf(message), 1);
            }
            console.log($scope.messages_selected);
        }

        $scope.get_msgs_page = function(page){
            Message.getMsgs($scope.folder, page).then(getMessagesByFolderSuccess, getMessagesByFolderError);
            $scope.page = page;
        };


        function getMessagesByFolderSuccess(data){
            //$scope.messages = data.data;
            data = angular.fromJson(data.data);


            $scope.messages = data.results;

            $scope.next_page = data.next;
            $scope.prev_page = data.previous;
            $scope.count = data.count;

            $scope.messages_selected = [];
            $scope.messages_select = false;

        };

        function getMessagesByFolderError(data){
            console.log('Error al cargar el inbox');
        }



        $scope.delete_bulk = function(){

            Message.delete_bulk($scope.messages_selected).then(deleteSuccess, deleteError);

            function deleteSuccess(data, headers, status){
                AlertNotification.success("Los mensajes seleccionados se eliminaron con exito");
                console.log(data.data);
                $scope.get_msgs_page($scope.page);
            }

            function deleteError(data, headers, status){
                AlertNotification.error("Error al intentar eliminar mensajes seleccionados");
            }
        }
        
        $scope.set_read_bulk = function(){
            Message.set_read_bulk($scope.messages_selected).then(setReadSuccess);

            function setReadSuccess(data, headers, status){
                $scope.get_msgs_page($scope.page);
            }
        }
        

        init();

        function init(){
            if($stateParams.folder != '' && $stateParams.folder != undefined){
                $scope.messages = $scope.loadMessages($stateParams.folder);
            }else{
                $scope.messages = $scope.loadMessages('inbox');
            }
        }


    }



})();
