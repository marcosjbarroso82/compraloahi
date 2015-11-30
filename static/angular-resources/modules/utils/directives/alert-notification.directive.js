/**
 * AlertNotification
 * @namespace appSearch.utils.directives
 */
(function ($, _) {
    'use strict';

    angular
        .module('appSearch.util.directives')
        .factory('AlertNotification', AlertNotification);


    AlertNotification.$inject = [];

    /**
     * @namespace AlertNotification
     */
    function AlertNotification() {
        /**
         * @name AlertNotification
         * @desc The factory to be returned
         */
        var AlertNotification = {
            error: error,
            success: success,
            warning: warning,
            info: info

        };

        return AlertNotification;

        ////////////////////

        function error(content, options) {
            toastr.error(content);
        }

        function success(content, options) {
            toastr.success(content);
        }

        function warning(content, options) {
            toastr.warning(content);
        }

        function info(content, options) {
            toastr.info(content);
        }


    }
})();