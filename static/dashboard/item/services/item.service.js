/**
 * Item
 * @namespace dashBoardApp.item.services
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.item.services')
        .factory('Item', Item);

    Item.$inject = ['$http'];

    /**
     * @namespace Item
     * @returns {Factory}
     */
    function Item($http) {
        var Items = {
            create: create,
            detail: detail,
            destroy: destroy,
            update: update,
            list:list,
            getCategories: getCategories
        };

        return Items;

        function list(){
            return $http.get('/api/v1/my-items/');
        }

        function detail(id){
            return $http.get('/api/v1/my-items/' + id + '/');
        }

        function destroy(id){
            return $http.delete('/api/v1/my-items/' + id + '/');
        }

        function getCategories(){
            return $http.get('/api/v1/categories/');
        }

        function create(item, images){
             var fd = new FormData();
            fd.append('data', angular.toJson(item));
            angular.forEach(images, function (val, key) {
                fd.append(key, val.file);
            });
            return $http.post('/api/v1/my-items/', fd, {
                headers: {'Content-Type': undefined},
                withCredentials: true,
                transformRequest: angular.identity
            });
        }

        function update(item, images){
            var fd = new FormData();
            fd.append('data', angular.toJson(item));
            angular.forEach(images, function (val, key) {
                fd.append(key, val.file);
            });
            return $http.put('/api/v1/my-items/' + item.id + '/', fd, {
                headers: {'Content-Type': undefined},
                withCredentials: true,
                transformRequest: angular.identity
            });
        }

    }

})();