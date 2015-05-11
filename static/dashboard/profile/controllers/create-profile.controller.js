/**
 * ProfileCreateController
 * @namespace dashBoardApp.profile.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.profile.controllers')
        .controller('ProfileCreateController', ProfileCreateController);

    ProfileCreateController.$inject = ['Profile', '$state', 'AlertNotification', '$filter'];

    /**
     * @namespace ProfileCreateController
     */
    function ProfileCreateController(Profile, $state, AlertNotification, $filter) {
        var vm = this;

        vm.profile = {};
        vm.submit = submit;
        vm.open = open;
        vm.removePhone = removePhone;
        vm.addPhone = addPhone;
        vm.profile.phones = [];

        init();

        /**
         * @name init
         * @desc function inizialize
         * @memberOf dashBoardApp.profile.controllers.ProfileCreateController
         */
        function init() {
            addPhone();
            vm.dateOptions = {
                formatYear: 'yy',
                startingDay: 1
            };
        }

        /**
         * @name activate
         * @desc Get Profile detail data
         * @memberOf dashBoardApp.profile.controllers.ProfileCreateController
         */
        function open($event) {
            $event.preventDefault();
            $event.stopPropagation();
            vm.opened = true;
        };


        /**
         * @name submit
         * @desc submit form to update profile
         * @memberOf dashBoardApp.profile.controllers.ProfileCreateController
         */
        function submit(){
            vm.profile.image = vm.img_profile;

            //Cast datetime to date.
            vm.profile.birth_date = $filter('date')(vm.profile.birth_date,'yyyy-MM-dd');
            Profile.create(vm.profile).then(updateSuccess, updateError);

            function updateSuccess(data){
                AlertNotification.success(data.data.message);
                $state.go('profile-detail');
            }

            function updateError(data){
                AlertNotification.error("Error al intentar cambiar los datos");
            }
        }

        /**
         * @name removePhone
         * @desc Delete phone to arrays phones
         * @param {Integer} Id to phone
         * @memberOf dashBoardApp.profile.controllers.ProfileCreateController
         */
        function removePhone(phone){
            vm.profile.phones.splice(vm.profile.phones.indexOf(phone), 1);
        }

        /**
         * @name addPhone
         * @desc add new row to array phones.
         * @memberOf dashBoardApp.profile.controllers.ProfileCreateController
         */
        function addPhone(){
            var phone = {};
            phone.id = vm.profile.phones[(vm.profile.phones.length -1)] + 1;
            if(!phone.id) phone.id = '';

            phone.type = "";
            phone.number = 0;

            //Add new obj phone to array phones
            vm.profile.phones.push(phone);
        }
    }

})();
