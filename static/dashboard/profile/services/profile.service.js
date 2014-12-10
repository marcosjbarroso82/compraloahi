/**
 * Profile
 * @namespace dashBoardApp.profile.services
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.profile.services')
        .factory('Profile', Profile);

    Profile.$inject = ['$http'];

    /**
     * @namespace Profile
     * @returns {Factory}
     */
    function Profile($http) {

        var Profile = {
            detail: detail,
            change_password: change_password
        };

        return Profile;


        /**
         * @name detail
         * @desc get Detail user profile
         * @returns {Promise}
         * @memberOf dashBoardApp.profile.services.Profile
         */
        function detail() {
            return $http.get('/api/v1/profile/');
        }

        /**
         * @name change_password
         * @Change password
         * @returns {Promise}
         * @memberOf dashBoardApp.profile.services.Profile
         */
        function change_password(password, new_password) {
            return $http.post('/account/change-password', {
                password: password,
                new_password: new_password
            });
        }

    }
})()