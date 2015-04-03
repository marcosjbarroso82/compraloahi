/**
 * Ad
 * @namespace dashBoardApp.ad.services
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.message.services')
        .factory('Message', Message);

    Message.$inject = ['$resource', '$http', '$q'];

    /**
     * @namespace Message
     * @returns {Factory}
     */
    function Message($resource, $http, $q) {
        var msgs = {
            getMsgs:getMsgs,
            getMsgThread:getMsgThread,
            getMsg: getMsg,
            reply: reply,
            delete_bulk: delete_bulk,
            set_read_bulk: set_read_bulk
        };

        function getMsgs(folder, page){
            if(page == 0){
                return $http.get('/api/v1/messages/' + folder);
            }else{
                return $http.get('/api/v1/messages/' + folder + "/?page=" + page);
            }

        }

        function getMsgThread(id){
            return $http.get('/api/v1/messages/thread/' + id);
        }

        function getMsg(id){
            return $http.get('/api/v1/messages/' + id);
        }

        function reply(id, msg){
            //var url = '/message/ajax-reply/' + id + '/?next=/accounts/profile/';
            var url = '/api/v1/messages-all/';
            return $q(function(resolve, reject) {
                $.post(url,
                    {
                        parent: id,
                        body: msg.body, csrfmiddlewaretoken: $.cookie('csrftoken')},
                    function(data) {
                        resolve('La respuesta se ha enviado con Exito');
                    })
                    .fail(function(){
                        reject('Error al enviar la respuesta');
                    });
            });
        }

        function delete_bulk(messages){
            return $http.patch('/api/v1/messages/delete-bulk/', messages);
        }
        
        function set_read_bulk(messages){
           return $http.patch('/api/v1/messages/set-read-bulk/', messages);
        }


        return msgs;
    }
})()
