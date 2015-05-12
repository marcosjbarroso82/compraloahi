/**
 * MessageThreadCtrl
 * @namespace dashBoardApp.MessageThreadCtrl.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.message.controllers')
        .controller('MessageThreadCtrl', MessageThreadCtrl);

    MessageThreadCtrl.$inject = ['$scope', 'Message', '$stateParams', '$q'];

    /**
     * @namespace MessageThreadCtrl
     */
    function MessageThreadCtrl($scope, Message, $stateParams, $q) {
        var vm = this;
        $scope.message = {};
        $scope.msgReply = {};

        $scope.loadMessageThread = function(id){
            vm.promiseRequest = Message.getMsgThread(id).then(getSuccess, getError);

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
                $scope.loadMessageThread($stateParams.id);
                $scope.msgReply = {};
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