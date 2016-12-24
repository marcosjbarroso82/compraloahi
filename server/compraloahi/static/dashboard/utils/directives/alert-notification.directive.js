/**
 * AlertNotification
 * @namespace dashBoardApp.utils.directives
 */
(function ($, _) {
    'use strict';

    angular
        .module('dashBoardApp.util.directives')
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
           //$notification.error('Error!', content);
        }

        function success(content, options) {
            toastr.success(content);

            //$notification.success('Success!', content);
        }

        function warning(content, options) {
            toastr.warning(content);
            //$notification.warning('Warning!!', content);
        }

        function info(content, options) {
            toastr.info(content);
            //$notification.info('Info!', content);
        }


    }
})();