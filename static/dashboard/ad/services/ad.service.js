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
            create: create,
            detail: detail,
            destroy: destroy,
            update: update,
            list:list,
            getCategories: getCategories
        };

        return Ads;

        function list(){
            return $http.get('/api/v1/my-ads/');
        }

        function detail(id){
            return $http.get('/api/v1/my-ads/' + id + '/');
        }

        function destroy(id){
            return $http.delete('/api/v1/my-ads/' + id + '/');
        }

        function getCategories(){
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

        function update(ad, images){
            var fd = new FormData();
            fd.append('data', angular.toJson(ad));
            angular.forEach(images, function (val, key) {
                fd.append(key, val.file);
            });
            return $http.put('/api/v1/my-ads/' + ad.id + '/', fd, {
                headers: {'Content-Type': undefined},
                withCredentials: true,
                transformRequest: angular.identity
            });
        }

    }

})();