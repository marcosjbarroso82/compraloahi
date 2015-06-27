/**
 * Profile
 * @namespace dashBoardApp.profile.services
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.profile.services')
        .factory('Profile', Profile);

    Profile.$inject = ['$http', '$q'];

    /**
     * @namespace Profile
     * @returns {Factory}
     */
    function Profile($http, $q) {

        var Profile = {
            detail: detail,
            change_password: change_password,
            update: update,
            create: create,
            upload_img: upload_img,
            is_username_valid: is_username_valid,
            set_profile: set_profile
        };

        var profile_cache = {};

        /**
         *
         * @param image
         * @returns {HttpPromise}
         */
        function upload_img(image) {
            var fd = new FormData();

            fd.append("image", image);
            return $http.post('/api/v1/change-image/', fd, {
                headers: {'Content-Type': undefined},
                withCredentials: true,
                transformRequest: angular.identity
            });
        }


        /**
         * @name detail
         * @desc get Detail user profile
         * @returns {Promise}
         * @memberOf dashBoardApp.profile.services.Profile
         */
        function detail() {
            if(profile_cache.id){
                var deferred = $q.defer();
                deferred.resolve({data:profile_cache});
                return deferred.promise;
            }else{
                return $http.get('/api/v1/profile/');
            }
        }

        /**
         * @name change_password
         * @Change password
         * @returns {Promise}
         * @memberOf dashBoardApp.profile.services.Profile
         */
        function change_password(user) {
            return $http.patch('/api/v1/change-password/', user);
        }

        /**
         * @name update
         * @desc update profile and user data
         * @param {Object} Object profile
         * @returns {Promise}
         * @memberOf dashBoardApp.profile.services.Profile
         */
        function update(profile){
            return $http.put('/api/v1/profile/', profile);
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


        function is_username_valid(username){
            return $http.get('/api/v1/username-is-unique/' + username + '/');
        }

        function set_profile(profile){
            profile_cache = profile;
        }

        return Profile;
    }
})()
