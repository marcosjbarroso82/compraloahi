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

    MessageThreadCtrl.$inject = ['Message', '$stateParams', 'AlertNotification', 'Authentication', '$scope'];

    /**
     * @namespace MessageThreadCtrl
     */
    function MessageThreadCtrl(Message, $stateParams, AlertNotification, Authentication, $scope) {
        var vm = this;
        vm.thread = [];
        vm.msgReply = {};
        vm.message_id = "";



        $scope.$watch( function () { return Authentication.msg_unread(); }, function (data) {
            vm.msgs_unread_count = Authentication.msg_unread();
          }, true);

        vm.loadMessageThread = function(id){
            vm.message_id = id;
            vm.promiseRequest = Message.getMsgThread(id).then(getSuccess, getError);

            function getSuccess(data){
                vm.thread = data.data;

                var msg = vm.thread[vm.thread.length - 1];
                if(msg && msg.is_new == true){
                    Message.set_read(msg).then(getReadSuccess);
                }
            }

            function getReadSuccess(data){
                Authentication.set_msg_read([{'id': vm.message_id}]);
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