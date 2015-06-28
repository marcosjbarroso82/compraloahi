/**
 * Store
 * @namespace dashBoardApp.store.services
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.store.services')
        .factory('Store', Store);

    Store.$inject = ['$http'];

    /**
     * @namespace Store
     * @returns {Factory}
     */
    function Store($http) {
        var store = {
            getConfig:getConfig,
            setConfig: setConfig,
            uploadImg: uploadImg,
            is_name_valid: is_name_valid
        };

        function getConfig(){
            return $http.get('/api/v1/store-config/');
        }

        function setConfig(data){
            return $http.put('/api/v1/store-config/', data);
        }

        function uploadImg(image){
            var fd = new FormData();

            fd.append("image", image);
            return $http.post('/api/v1/change-logo/', fd, {
                headers: {'Content-Type': undefined},
                withCredentials: true,
                transformRequest: angular.identity
            });
        }

        function is_name_valid(slug){
            return $http.get('/api/v1/store-name-is-unique/' + slug + '/');
        }

        return store;
    }
})()
