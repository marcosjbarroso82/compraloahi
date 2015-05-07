/**
 * AlertNotification
 * @namespace dashBoardApp.utils.directives
 */
(function ($, _) {
    'use strict';

    angular
        .module('dashBoardApp.util.directives')
        .factory('AlertNotification', AlertNotification);


    AlertNotification.$inject = ['snackbar'];

    /**
     * @namespace AlertNotification
     */
    function AlertNotification(snackbar) {
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
            snackbar.create('<i class="fa fa-times-circle" style="color: #CD4945;"> </i> Error : ' + content);
           //$notification.error('Error!', content);
        }

        function success(content, options) {
            snackbar.create('<i class="fa fa-check-circle" style="color: #0DAD9E;"> </i> Success : ' + content);

            //$notification.success('Success!', content);
        }

        function warning(content, options) {
            snackbar.create('<i class="fa fa-exclamation-circle" style="color: #CFAE45;"> </i> warning : ' + content);
            //$notification.warning('Warning!!', content);
        }

        function info(content, options) {
            snackbar.create('<i class="fa fa-info-circle" style="color: #2B6A94;"> </i> Info : ' + content, 5000);
            //$notification.info('Info!', content);
        }


    }
})();