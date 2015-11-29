(function () {
    'use strict';

    angular
        .module('dashBoardApp.profile.controllers')
        .controller('ConfigPrivacityController', ConfigPrivacityController);

    ConfigPrivacityController.$inject = ['Profile','AlertNotification', '$state'];

    /**
     * @namespace ConfigPrivacityController
     */
    function ConfigPrivacityController(Profile, AlertNotification, $state) {
        var vm = this;

        vm.config = {};

        vm.submit = submit;


        activate();

        function activate(){
            Profile.get_config_privacity().then(getConfigPrivacitySuccess, getConfigPrivacityError);

            function getConfigPrivacitySuccess(data){
                vm.config = data.data
            }

            function getConfigPrivacityError(data){
                AlertNotification.error("Error al intentar recuperar su configuracion, vuelva a intentarlo mas tarde");
            }
        }


        function submit(){
           Profile.set_config_privacity(vm.config).then(setConfigPrivacitySuccess, setConfigPrivacityError);

            function setConfigPrivacitySuccess(data){
                AlertNotification.success("Se ha cambiado su configuracion de privacidad correctamente");
                $state.go('profile-detail');
            }

            function setConfigPrivacityError(data){
                AlertNotification.error("Error al intentar actualizar su configuracion de privacidad, vuelva a intentarlo mas tarde, o pongase en contacto con nosotros");
            }
        }
    }

})();
