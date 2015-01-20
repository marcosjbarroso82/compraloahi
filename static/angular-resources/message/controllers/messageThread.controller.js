/**
 * MessageThreadCtrl
 * @namespace App.MessageThreadCtrl.controllers
 */
(function () {
    'use strict';

    angular
        .module('App.message.controllers')
        .controller('MessageThreadCtrl', MessageThreadCtrl);

    MessageThreadCtrl.$inject = ['$scope', 'Message', '$stateParams', '$q'];

    /**
     * @namespace MessageThreadCtrl
     */
    function MessageThreadCtrl($scope, Message, $stateParams, $q) {
        $scope.message = {};
        $scope.msgReply = {};

        $scope.loadMessageThread = function(id){
            Message.getMsgThread(id).then(getSuccess, getError);

            function getSuccess(data){
                $scope.message = data.data;
            };

            function getError(data){
                console.log('Error al cargar el mensaje');
            }
        }

        $scope.reply = function(){

            Message.reply($stateParams.id, $scope.msgReply)
                .then(replySuccess, replyError);

            function replySuccess(data){
                console.log('replySuccess');
                console.log(data);
            }

            function replyError(data){
                console.log('replyError');
                console.log("ERROR REPLY" + data);
            }
        }

        console.log($stateParams);
        $scope.message = $scope.loadMessageThread($stateParams.id);
    }
})();