/**
 * ProfileDetailController
 * @namespace dashBoardApp.profile.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.profile.controllers')
        .controller('ProfileDetailController', ProfileDetailController);

    ProfileDetailController.$inject = ['Profile', 'AlertNotification', '$filter', '$scope'];

    /**
     * @namespace ProfileDetailController
     */
    function ProfileDetailController(Profile, AlertNotification, $filter, $scope) {
        var vm = this;

        vm.profile = undefined;

        vm.submit = submit;
        vm.removePhone = removePhone;
        vm.addPhone = addPhone;

        vm.upload_img = upload_img;

        activate();

        /**
         * @name activate
         * @desc Get Profile detail data
         * @memberOf dashBoardApp.authentication.controllers.ProfileDetailController
         */
        function activate() {
            vm.promiseRequest = Profile.detail().then(detailSuccess, detailError);

            function detailSuccess(data){
                vm.profile = data.data;
                vm.profile.birth_date_input = angular.copy(new Date(vm.profile.birth_date));
            }

            function detailError(data){
                console.log(data);
            }

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


        /**
         * @name submit
         * @desc submit form to update profile
         * @memberOf dashBoardApp.profile.controllers.ProfileUpdateController
         */
        function submit(){
            //Cast datetime to date.
            // TODO: Se rompe el formato fecha para el input al hacer el filtro
            vm.profile.birth_date = angular.copy($filter('date')(vm.profile.birth_date_input,'yyyy-MM-dd'));
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