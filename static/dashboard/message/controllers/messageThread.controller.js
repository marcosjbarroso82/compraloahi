/**
 * MessageThreadCtrl
 * @namespace dashBoardApp.MessageThreadCtrl.controllers
 */
var debug = {};
(function () {
    'use strict';

    angular
        .module('dashBoardApp.message.controllers')
        .controller('MessageThreadCtrl', MessageThreadCtrl);

    MessageThreadCtrl.$inject = ['Message', '$stateParams', 'AlertNotification'];

    /**
     * @namespace MessageThreadCtrl
     */
    function MessageThreadCtrl(Message, $stateParams, AlertNotification) {
        var vm = this;
        vm.thread = [];
        vm.msgReply = {};
        vm.message_id;

        vm.loadMessageThread = function(id){
            vm.message_id = id;
            vm.promiseRequest = Message.getMsgThread(id).then(getSuccess, getError);

            function getSuccess(data){
                vm.thread = data.data;
            }

            function getError(data){
                AlertNotification.error('Error al cargar el mensaje');
            }
        }

        vm.reply = function(){
            Message.reply(vm.msgReply, vm.message_id)
                .then(replySuccess, replyError);

            function replySuccess(data){
                vm.thread.push(data.data);
                vm.msgReply = {};
                AlertNotification.success("El mensaje fue enviado correctamente");
            }

            function replyError(data){
                AlertNotification.success("Error al intentar responder el mensaje");
            }
        }

        vm.loadMessageThread($stateParams.id);
    }
})();