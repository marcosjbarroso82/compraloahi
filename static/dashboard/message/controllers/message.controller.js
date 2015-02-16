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

        $scope.title = "Inbox";

        $scope.loadMessages = function(folder){
            Message.getMsgs(folder, 0).then(getMessagesByFolderSuccess, getMessagesByFolderError);
            $scope.folder = folder;
            if($scope.folder == 'inbox'){
                $scope.title = "Inbox";
                $scope.active_inbox = "active";
                $scope.active_sent = "";
            }else{
                $scope.title = "Sent";
                $scope.active_inbox = "";
                $scope.active_sent = "active";

            }

        }

        $scope.select_messages = function(){
            angular.forEach($scope.messages, function(message){
               message.selected = $scope.messages_select;
            });
        }


        $scope.get_msgs_page = function(page){
            Message.getMsgs($scope.folder, page).then(getMessagesByFolderSuccess, getMessagesByFolderError);
        };


        function getMessagesByFolderSuccess(data){
            //$scope.messages = data.data;
            data = angular.fromJson(data.data);

            // Rewrite Next and Previous
            data.next = data.next ? getPageFromUrl(data.next) : "";
            data.previous = data.previous ? getPageFromUrl(data.previous) : "";

            $scope.messages = data.results;

            $scope.next_page = data.next;
            $scope.prev_page = data.previous;
        };

        function getMessagesByFolderError(data){
            console.log('Error al cargar el inbox');
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


        /**
         * Gets a page parameter from url
         * @param {String} url
         * @return {String} page
         */
        function getPageFromUrl(url) {
            url = url.split(/\?|\&/);
            //previous = previous.split(/\?|\&/);
            var params = [];
            var page = "";
            url.forEach( function(str_param) {
                if (str_param) {
                    var param = str_param.split("=");
                    if (param[0] == 'page') {
                        page = param[1];
                   }
                }
            });
            return page;
        }


    }



})();