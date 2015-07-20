/**
 * Ad
 * @namespace dashBoardApp.ad.services
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.message.services')
        .factory('Message', Message);

    Message.$inject = ['$http'];

    /**
     * @namespace Message
     * @returns {Factory}
     */
    function Message($http) {
        var msgs = {
            getMsgs:getMsgs,
            getUnreadCount:getUnreadCount,
            getMsgThread:getMsgThread,
            getMsg: getMsg,
            reply: reply,
            delete_bulk: delete_bulk,
            set_read_bulk: set_read_bulk
        };

        function getMsgs(folder, page){
            if(page == 0){
                return $http.get('/api/v1/msgs/' + folder);
            }else{
                return $http.get('/api/v1/msgs/' + folder + "/?page=" + page);
            }
        }

        function getUnreadCount(){
            return $http.get('/api/v1/msgs/unread-count/');
        }

        function getMsgThread(id){
            return $http.get('/api/v1/msgs/thread/' + id);
        }

        function getMsg(id){
            return $http.get('/api/v1/msgs/' + id);
        }

        function reply(msg){
            return $http.post('/api/v1/msgs/', msg);

        }

        function delete_bulk(messages){
            return $http.patch('/api/v1/msgs/delete-bulk/', messages);
        }
        
        function set_read_bulk(messages){
           return $http.patch('/api/v1/msgs/set-read-bulk/', messages);
        }


        return msgs;
    }
})()
