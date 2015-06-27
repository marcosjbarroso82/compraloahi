/**
 * ProfileDetailController
 * @namespace dashBoardApp.profile.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.profile.controllers')
        .controller('ProfileDetailController', ProfileDetailController);

    ProfileDetailController.$inject = ['Profile', 'AlertNotification', '$scope'];

    /**
     * @namespace ProfileDetailController
     */
    function ProfileDetailController(Profile, AlertNotification, $scope) {
        var vm = this;

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
                Profile.set_profile(vm.profile);
                if (vm.profile.birth_date) {
                    vm.profile.birth_date_input = angular.copy(new Date(vm.profile.birth_date));
                }
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

    }


})();