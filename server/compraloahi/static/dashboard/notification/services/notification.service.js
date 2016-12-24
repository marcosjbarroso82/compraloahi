/**
 * Notification
 * @namespace dashBoardApp.notification.services
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.notification.services')
        .factory('Notification', Notification);

    Notification.$inject = ['$http'];

    /**
     * @namespace Notification
     * @returns {Factory}
     */
    function Notification($http) {

        var notification = {
            getConfigNotification: getConfigNotification,
            configNotification: configNotification
        };

        function getConfigNotification(folder, page){
            return $http.get('/api/v1/notifications-config/');
        }

        function configNotification(configs){
            return $http.put('/api/v1/notifications-config/', configs);
        }

        return notification;
    }
})();
