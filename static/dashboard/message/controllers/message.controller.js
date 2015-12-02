/**
 * MessageCtrl
 * @namespace dashBoardApp.message.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.message.controllers')
        .controller('MessageCtrl', MessageCtrl);

    MessageCtrl.$inject = ['Message', 'AlertNotification', '$stateParams', 'Authentication', '$scope'];

    /**
     * @namespace MessageCtrl
     */
    function MessageCtrl(Message, AlertNotification, $stateParams, Authentication, $scope) {
        var vm = this;

        // Declare functions
        vm.loadMessages = loadMessages;
        vm.select_all_messages = select_all_messages;
        vm.select_message = select_message;
        vm.delete_bulk = delete_bulk;
        vm.set_read_bulk = set_read_bulk;

        // Declare vars
        vm.messages = [];
        vm.message = {};
        vm.messages_selected = [];
        vm.page = 1;
        vm.count = 0;

        vm.folder = 'inbox';


        $scope.$watch( function () { return Authentication.msg_unread(); }, function (data) {
            vm.msgs_unread_count = Authentication.msg_unread();
        }, true);

        init();

        function init(){
            vm.folder = $stateParams.folder = typeof $stateParams.folder !== 'undefined' ? $stateParams.folder : 'inbox';
            vm.loadMessages();
        }

        function loadMessages(page_nro){
            page_nro = typeof page_nro !== 'undefined' ? page_nro : 1;
            if(page_nro){
                vm.promiseRequest = Message.getMsgs(vm.folder, page_nro).then(getMessagesByFolderSuccess, getMessagesByFolderError);
                vm.folder = vm.folder;
                vm.page = page_nro;
            }

        }

        function select_all_messages(){


            angular.forEach(vm.messages, function(message){
                message.selected = vm.messages_select_all;

            });

            if(vm.messages_select_all){
                vm.messages_selected = vm.messages;
            }else{
                vm.messages_selected = [];
            }
        }

        function select_message(message){
            // If message has state selected add to array messages_selected, else, remove.
            if(message.selected){
                vm.messages_selected.push(message);
            }else{
                vm.messages_selected.splice(vm.messages_selected.indexOf(message), 1);
            }
        }


        function getMessagesByFolderSuccess(data){
            data = angular.fromJson(data.data);
            vm.messages = data.results;
            vm.next_page = data.next;
            vm.prev_page = data.previous;
            vm.count = data.count;
            vm.messages_selected = [];
            vm.messages_select_all = false;
        }

        function getMessagesByFolderError(data){
            AlertNotification.error("Error al intentar consultar mensajes, intenta mas tarde.");
        }

        function delete_bulk(){
            vm.promiseRequest = Message.delete_bulk(vm.messages_selected).then(deleteSuccess, deleteError);

            function deleteSuccess(data, headers, status){
                AlertNotification.success("Los mensajes seleccionados se eliminaron con exito");
                vm.loadMessages(vm.page);
            }

            function deleteError(data, headers, status){
                AlertNotification.error("Error al intentar eliminar mensajes seleccionados");
            }
        }

        function set_read_bulk(){
            //var msgs_set_read = [];
//            angular.forEach(vm.messages_selected, function(message){
//                if(message.read_at == null){
//                    var msg = angular.copy(message);
//                    msgs_set_read.push(msg);
//                }
//
//            });
            Message.set_read_bulk(vm.messages_selected).then(setReadBulkSuccess, setReadBulkError);

            function setReadBulkSuccess(data, headers, status){
                AlertNotification.success("Los seleccionados mensajes fueron marcados como leido.");
                var read_msgs = [];
                for(var i=0; i < vm.messages_selected.length; i++){
                    if(vm.messages_selected[i].read_at == null){
                        vm.messages_selected[i].read_at = "Leido";
                        read_msgs.push(vm.messages_selected[i]);
                    }
                    vm.messages_selected[i].selected = false;
                }

                Authentication.set_msg_read(read_msgs);


                // Clear array to selected messages
                vm.messages_selected = [];
                // Clear Checkbox to select all
                vm.messages_select_all = false;


            }

            function setReadBulkError(data){
                AlertNotification.error("Error al intentar marcar todos los mensajes como leido. Intente nuevamente");
            }
        }




    }

})();
