/**
 * MessageCtrl
 * @namespace dashBoardApp.message.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.message.controllers')
        .controller('MessageCtrl', MessageCtrl);

    MessageCtrl.$inject = ['Message', 'AlertNotification', '$stateParams'];

    /**
     * @namespace MessageCtrl
     */
    function MessageCtrl(Message, AlertNotification, $stateParams) {
        var vm = this;

        vm.messages = {};
        vm.message = {};
        vm.messages_selected = [];
        vm.page = 1;
        vm.count = 0;

        vm.loadMessages = function(folder){
            vm.promiseRequest = Message.getMsgs(folder, 0).then(getMessagesByFolderSuccess, getMessagesByFolderError);
            vm.folder = folder;
            
        }

        vm.select_all_messages = function(){
            angular.forEach(vm.messages, function(message){
               message.selected = vm.messages_select;
            });

            if(vm.messages_select){
                vm.messages_selected = vm.messages;
            }else{
                vm.messages_selected = [];
            }
        }
        
        vm.select_message = function(message){
            // If message has state selected add to array messages_selected, else, remove.
            if(message.selected){
                vm.messages_selected.push(message);
            }else{
                vm.messages_selected.splice(vm.messages_selected.indexOf(message), 1);
            }
            console.log(vm.messages_selected);
        }

        vm.get_msgs_page = function(page){
            vm.promiseRequest = Message.getMsgs(vm.folder, page).then(getMessagesByFolderSuccess, getMessagesByFolderError);
            vm.page = page;
        };


        function getMessagesByFolderSuccess(data){
            //vm.messages = data.data;
            data = angular.fromJson(data.data);


            vm.messages = data.results;

            vm.next_page = data.next;
            vm.prev_page = data.previous;
            vm.count = data.count;

            vm.messages_selected = [];
            vm.messages_select = false;

        };

        function getMessagesByFolderError(data){
            console.log('Error al cargar el inbox');
        }



        vm.delete_bulk = function(){

            vm.promiseRequest = Message.delete_bulk(vm.messages_selected).then(deleteSuccess, deleteError);

            function deleteSuccess(data, headers, status){
                AlertNotification.success("Los mensajes seleccionados se eliminaron con exito");
                console.log(data.data);
                vm.get_msgs_page(vm.page);
            }

            function deleteError(data, headers, status){
                AlertNotification.error("Error al intentar eliminar mensajes seleccionados");
            }
        }
        
        vm.set_read_bulk = function(){
            Message.set_read_bulk(vm.messages_selected).then(setReadSuccess);

            function setReadSuccess(data, headers, status){
                vm.get_msgs_page(vm.page);
            }
        }
        

        init();

        function init(){
            if($stateParams.folder != '' && $stateParams.folder != undefined){
                vm.messages = vm.loadMessages($stateParams.folder);
            }else{
                vm.messages = vm.loadMessages('inbox');
            }
        }


    }



})();
