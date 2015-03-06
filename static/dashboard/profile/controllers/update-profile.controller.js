/**
 * ProfileUpdateController
 * @namespace dashBoardApp.profile.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.profile.controllers')
        .controller('ProfileUpdateController', ProfileUpdateController);

    ProfileUpdateController.$inject = ['Profile', '$state', 'Snackbar', '$filter'];

    /**
     * @namespace ProfileUpdateController
     */
    function ProfileUpdateController(Profile, $state, Snackbar, $filter) {
        var vm = this;

        vm.profile = undefined;
        vm.submit = submit;
        vm.open = open;
        vm.removePhone = removePhone;
        vm.addPhone = addPhone;

        init();

        /**
         * @name init
         * @desc function inizialize
         * @memberOf dashBoardApp.profile.controllers.ProfileUpdateController
         */
        function init() {

            Profile.detail().then(detailSuccess, detailError);

            function detailSuccess(data){
                vm.profile = data.data;
            }

            function detailError(data){
                Snackbar.error("Error al cargar los datos de su perfil. Intente cargar de nuevo la pagina");
            }

            vm.dateOptions = {
                formatYear: 'yy',
                startingDay: 1
            };
        }

        /**
         * @name activate
         * @desc Get Profile detail data
         * @memberOf dashBoardApp.profile.controllers.ProfileUpdateController
         */
        function open($event) {
            $event.preventDefault();
            $event.stopPropagation();
            vm.opened = true;
        };


        /**
         * @name submit
         * @desc submit form to update profile
         * @memberOf dashBoardApp.profile.controllers.ProfileUpdateController
         */
        function submit(){
            vm.profile.image = vm.img_profile;

            //Cast datetime to date.
            vm.profile.birth_date = $filter('date')(vm.profile.birth_date,'yyyy-MM-dd');
            Profile.update(vm.profile).then(updateSuccess, updateError);

            function updateSuccess(data){
                Snackbar.show(data.data.message);
                $state.go('profile-detail');
            }

            function updateError(data){
                Snackbar.error(data.data.message);

            }
        }

        /**
         * @name removePhone
         * @desc Delete phone to arrays phones
         * @param {Integer} Id to phone
         * @memberOf dashBoardApp.profile.controllers.ProfileUpdateController
         */
        function removePhone(phone){
            vm.profile.phones.splice(vm.profile.phones.indexOf(phone), 1);
        }

        /**
         * @name addPhone
         * @desc add new row to array phones.
         * @memberOf dashBoardApp.profile.controllers.ProfileUpdateController
         */
        function addPhone(){
            var phone = {};
            phone.id = vm.profile.phones[(vm.profile.phones.length -1)] + 1;
            phone.type = "";
            phone.number = 0;
            //Add new obj phone to array phones
            vm.profile.phones.push(phone);
        }
    }

})();
