/**
 * ConfigNotificationCtrl
 * @namespace
 */
 (function () {
    'use strict';

    angular
    .module('dashBoardApp.notification.controllers')
    .controller('ConfigNotificationCtrl', ConfigNotificationCtrl);

    ConfigNotificationCtrl.$inject = ['Notification', 'AlertNotification', '$state'];

    /**
     * @namespace ConfigNotificationCtrl
     */
     function ConfigNotificationCtrl(Notification, AlertNotification, $state) {

        var vm = this;

        vm.configs = {};
        vm.submit = submit;
        
        function activate(){

            vm.promiseRequest = Notification.getConfigNotification().then(success, error);

            function success(data){
                vm.configs = data.data;
            }

            function error(data){
                AlertNotification.error("Error al intentar cargar la configuracion");
            }
        }

        activate();



        function submit(){
            Notification.configNotification(vm.configs).then(success, error);

            function success(data){
                AlertNotification.success("Notificaciones configuradas conrrectamente.");
                $state.go('profile-detail');
            }

            function error(data){
                AlertNotification.error("Se produjo un error al intentar configurar las notificaciones");
            }
        }

    }
})();
