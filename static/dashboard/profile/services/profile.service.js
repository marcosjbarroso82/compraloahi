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
            change_password: change_password,
            update: update,
            create: create
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
        function change_password(user) {
            return $http.patch('/api/v1/change-password/', {
                password: user.password,
                new_password: user.new_password,
                new_password_repeat: user.new_password_repeat
            });
        }

        /**
         * @name update
         * @desc update profile and user data
         * @param {Object} Object profile
         * @returns {Promise}
         * @memberOf dashBoardApp.profile.services.Profile
         */
        function update(profile){
            var fd = new FormData();

            fd.append('birth_date', profile.birth_date);
            fd.append('user', angular.toJson(profile.user));
            fd.append('phones', angular.toJson(profile.phones));
            fd.append('image', profile.image);


            return $http.put('/api/v1/profile/'+ profile.id + '/', fd, {
                //headers: {'Content-Type': undefined},
                headers: {'Content-Type': undefined},
                //withCredentials: true,
                transformRequest: angular.identity

            })
        }

        /**
         * @name create
         * @desc create profile and user data
         * @param {Object} Object profile
         * @returns {Promise}
         * @memberOf dashBoardApp.profile.services.Profile
         */
        function create(profile){
            var fd = new FormData();

            fd.append('birth_date', profile.birth_date);
            fd.append('user', angular.toJson(profile.user));
            fd.append('phones', angular.toJson(profile.phones));
            fd.append('image', profile.image);
            console.log(profile);
            return $http.post('/api/v1/profile/create/', fd, {
                headers: {'Content-Type': undefined},
                withCredentials: true,
                transformRequest: angular.identity
            })
        }

    }
})()
