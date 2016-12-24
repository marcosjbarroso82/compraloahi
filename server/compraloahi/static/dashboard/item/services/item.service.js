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
            return $http.get('/api/v1/user-items/');
        }

        function detail(id){
            return $http.get('/api/v1/user-items/' + id + '/');
        }

        function destroy(id){
            return $http.delete('/api/v1/user-items/' + id + '/');
        }

        function getCategories(){
            return $http.get('/api/v1/categories/');
        }

        function create(item){
            return $http.post('/api/v1/user-items/', item);
        }

        function update(item){
            return $http.put('/api/v1/user-items/' + item.id + '/', item);
        }

    }

})();