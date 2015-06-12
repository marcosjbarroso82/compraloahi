/**
 * Ad
 * @namespace dashBoardApp.ad.services
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.ad.services')
        .factory('Ad', Ad);

    Ad.$inject = ['$http'];

    /**
     * @namespace Ad
     * @returns {Factory}
     */
    function Ad($http) {
        var Ads = {
            getAll:getAll,
            destroy: destroy,
            getAllCategories: getAllCategories,
            create: create
        };
        return Ads;

        function getAll(){
            return $http.get('/api/v1/my-ads/');
        }

        function destroy(id){
            return $http.delete('/api/v1/my-ads/' + id + '/');
        }

        function getAllCategories(){
            return $http.get('/api/v1/categories/');
        }

        function create(ad, images){
             var fd = new FormData();
            fd.append('data', angular.toJson(ad));
            angular.forEach(images, function (val, key) {
                fd.append(key, val.file);
            });
            return $http.post('/api/v1/my-ads/', fd, {
                headers: {'Content-Type': undefined},
                withCredentials: true,
                transformRequest: angular.identity
            });
        }

    }

})();