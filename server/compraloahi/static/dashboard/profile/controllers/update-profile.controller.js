/**
 * ProfileUpdateController
 * @namespace dashBoardApp.profile.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.profile.controllers')
        .controller('ProfileUpdateController', ProfileUpdateController);

    ProfileUpdateController.$inject = ['Profile', '$scope', 'AlertNotification', '$state', 'Authentication'];

    /**
     * @namespace ProfileUpdateController
     */
    function ProfileUpdateController(Profile, $scope, AlertNotification, $state, Authentication) {
        var vm = this;

        vm.profile = {};
        vm.profile.user = {};
        vm.profile.usermame = "";
        vm.submit = submit;
        vm.open = open;
        vm.removePhone = removePhone;
        vm.addPhone = addPhone;

        vm.username_unique = false;
        vm.username_is_valid = false;

        vm.upload_img = upload_img;


        activate();

        /**
         * @name init
         * @desc function inizialize
         * @memberOf dashBoardApp.profile.controllers.ProfileUpdateController
         */
        function activate() {
            vm.profile = angular.copy(Authentication.profile);
        }

        /**
         * @name submit
         * @desc submit form to update profile
         * @memberOf dashBoardApp.profile.controllers.ProfileUpdateController
         */
        function submit(){
            Profile.update(vm.profile).then(updateSuccess, updateError);

            function updateSuccess(data){
                Authentication.profile = angular.copy(data.data);
                AlertNotification.success("El perfil se modifico correctamente.");
                $state.go('profile-detail');
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
            //Itemd new obj phone to array phones
            vm.profile.phones.push(phone);
        }



        function upload_img(){

            if (vm.img_profile && 'name' in vm.img_profile){
                vm.promise_img = Profile.upload_img(vm.img_profile).then(ChangeImgSuccess, ChangeImgError);
            }

            function ChangeImgSuccess(data, status, headers, config){
                vm.profile.thumbnail_200x200 = data.data.image_url;
                $scope.img_profile = {};
            }

            function ChangeImgError(data, status, headers, config){
                AlertNotification.error(data.error);
            }
        }

        $scope.$watch('vm.img_profile', function(){
            upload_img();
        });


        $scope.$watch('vm.profile.user.username', function(newValue, oldValue){
            if(String(vm.profile.user.username).length > 3){
                Profile.is_username_valid(vm.profile.user.username).then(isUsernameValidSuccess);
            }

            function isUsernameValidSuccess(data){
                if (data.data.is_valid != 'true'){
                    vm.username_unique = true;
                    vm.username_is_valid = false;
                }else{
                    vm.username_unique = false;
                    vm.username_is_valid = true;
                }
            }
        });
    }

})();
