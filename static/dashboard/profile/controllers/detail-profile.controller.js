/**
 * ProfileDetailController
 * @namespace dashBoardApp.profile.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.profile.controllers')
        .controller('ProfileDetailController', ProfileDetailController);

    ProfileDetailController.$inject = ['Profile', 'AlertNotification', '$filter'];

    /**
     * @namespace ProfileDetailController
     */
    function ProfileDetailController(Profile, AlertNotification, $filter) {
        var vm = this;

        vm.profile = undefined;

        vm.submit = submit;
        vm.removePhone = removePhone;
        vm.addPhone = addPhone;

        activate();

        /**
         * @name activate
         * @desc Get Profile detail data
         * @memberOf dashBoardApp.authentication.controllers.ProfileDetailController
         */
        function activate() {
            Profile.detail().then(detailSuccess, detailError);

            function detailSuccess(data){
                vm.profile = data.data;
            }

            function detailError(data){
                console.log(data);
            }

        }


        /**
         * @name submit
         * @desc submit form to update profile
         * @memberOf dashBoardApp.profile.controllers.ProfileUpdateController
         */
        function submit(){
            //Cast datetime to date.
            vm.profile.birth_date = $filter('date')(vm.profile.birth_date,'yyyy-MM-dd');
            Profile.update(vm.profile).then(updateSuccess, updateError);

            function updateSuccess(data){
                AlertNotification.success("El perfil se modifico correctamente.");
                //$state.go('profile-detail');
                vm.profileEdit = false;
            }

            function updateError(data){
                AlertNotification.error("Error al modificar el perfil");

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