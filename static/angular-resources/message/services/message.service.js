/**
 * Ad
 * @namespace App.ad.services
 */
(function () {
    'use strict';

    angular
        .module('App.message.services')
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
            delete_bulk: delete_bulk
        };

        function getMsgs(folder){
            return $http.get('/api/v1/messages/' + folder);
        }

        function getMsgThread(id){
            return $http.get('/api/v1/messages/thread/' + id);
        }

        function getMsg(id){
            return $http.get('/api/v1/messages/' + id);
        }

        function reply(id, msg){
            var url = '/message/ajax-reply/' + id + '/?next=/accounts/profile/';
            return $q(function(resolve, reject) {
                $.post(url,
                    {body: msg.body, csrfmiddlewaretoken: $.cookie('csrftoken')},
                    function(data) {
                        resolve('La respuesta se ha enviado con Exito');
                    })
                    .fail(function(){
                        reject('Error al enviar la respuesta');
                    });
            });
        }

        function delete_bulk(messages){
            console.log("DELETE_BULK");
            console.log(messages);
            return $http.patch('/api/v1/messages/delete-bulk/', messages);
        }

        /*
         // We replaced this function with Reply() because aparently we have problems with the content type
         // In the future, we'll try again
         return $http({
         url: '/message/ajax-reply/' + id + '/?next=/accounts/profile/',
         dataType: 'application/x-www-form-urlencoded; charset=UTF-8',
         method: 'POST',
         data: 'body= +aaaaaaaaaaccccccccccccccccccccccccccsssssssss',
         headers: {'Content-Type': undefined}
         });
         */

        return msgs;
    }
})()